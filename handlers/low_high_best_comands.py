from loader import bot
from telebot.types import Message
from loguru import logger
import datetime
from states.user_inputs import UserInputState
from api.first_request import find_destination
from keyboards.inline import city_buttons


@bot.message_handler(commands=['lowprice', 'highprice', 'bestdeal'])
def low_high_best_handler(message: Message) -> None:
    bot.set_state(message.chat.id, UserInputState.command)
    with bot.retrieve_data(message.chat.id) as data:
        data.clear()
        logger.info('Запоминаем выбранную команду: ' + message.text)
        data['command'] = message.text
        data['date_time'] = datetime.datetime.utcnow().strftime('%d.%m.%Y %H:%M:%S')
        data['telegram_id'] = message.from_user.id
        data['chat_id'] = message.chat.id
    bot.set_state(message.chat.id, UserInputState.input_city)
    bot.send_message(message.from_user.id, "Введите город в котором нужно найти отель: ")


@bot.message_handler(state=UserInputState.input_city)
def input_city(message: Message) -> None:
    """
        Здесь пользователь вводит название интересующего его города, который бот запоминает и
        отправляет сообщение функцию find_city(message), проверить наличие города
        :param message:
    """
    with bot.retrieve_data(message.chat.id) as data:
        data['input_city'] = message.text
        logger.info('Пользователь ввел город: ' + message.text)
        region_ids = find_destination(message.text)
        city_buttons.show_cities_buttons(message, region_ids)


@bot.message_handler(state=UserInputState.quantity_hotels)
def input_quantity(message):
    if message.text.isdigit():
        if 0 < int(message.text) < 25:
            logger.info('Input quantity hotels' + message.text)
            with bot.retrieve_data(message.chat.id) as data:
                data['quantity_hotels'] = message.text
                print(data)
            bot.set_state(message.chat.id, UserInputState.priceMin)
            bot.send_message(message.chat.id, 'Input price minimum:')
        else:
            bot.send_message(message.chat.id, 'the number must be from 1 to 25')
    else:
        bot.send_message(message.chat.id, 'It should be a number')


@bot.message_handler(state=UserInputState.priceMin)
def input_price_min(message):
    if message.text.isdigit():
        logger.info('Input minimum price' + message.text)
        with bot.retrieve_data(message.chat.id) as data:
            data['price_min'] = message.text
        bot.set_state(message.chat.id, UserInputState.priceMax)
        bot.send_message(message.chat.id, 'Input price maximum:')
    else:
        bot.send_message(message.chat.id, 'It should be a number')


@bot.message_handler(state=UserInputState.priceMax)
def input_price_max(message):
    if message.text.isdigit():
        logger.info('Input maximum price' + message.text)
        with bot.retrieve_data(message.chat.id) as data:
            data['price_max'] = message.text
        print(data)
    else:
        bot.send_message(message.chat.id, 'It should be a number')

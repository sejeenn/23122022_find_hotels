from loader import bot
from telebot.types import Message
from loguru import logger
import datetime
from states.user_inputs import UserInputState
from api.first_request import find_destination
import keyboards.inline
from keyboards.calendar import calendar


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
        keyboards.inline.city_buttons.show_cities_buttons(message, region_ids)


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
        logger.info('Input minimum price: ' + message.text)
        with bot.retrieve_data(message.chat.id) as data:
            data['price_min'] = message.text
        bot.set_state(message.chat.id, UserInputState.priceMax)
        bot.send_message(message.chat.id, 'Input price maximum:')
    else:
        bot.send_message(message.chat.id, 'It should be a number')


@bot.message_handler(state=UserInputState.priceMax)
def input_price_max(message):
    if message.text.isdigit():
        logger.info('Input maximum price: ' + message.text)
        with bot.retrieve_data(message.chat.id) as data:
            if int(data['price_min']) < int(message.text):
                data['price_max'] = message.text
                keyboards.inline.photo_need.show_buttons_photo_need_yes_no(message)
            else:
                bot.send_message(message.chat.id, 'Price maximum should be more than minimum! Input again!')

    else:
        bot.send_message(message.chat.id, 'It should be a number')


@bot.message_handler(state=UserInputState.photo_count)
def input_photo_quantity(message):
    if message.text.isdigit():
        if 1 < int(message.text) < 10:
            logger.info('Input photo quantity: ' + message.text)
            with bot.retrieve_data(message.chat.id) as data:
                data['photo_count'] = message.text
            calendar.my_calendar(message)

        else:
            bot.send_message(message.chat.id, 'Number of photos from 1 to 10! Input again!')
    else:
        bot.send_message(message.chat.id, 'Only numbers! Input again!')


def check_command(message, data):
    logger.info('Check which command is entered')
    if data['command'] == '/bestdeal':
        data['sort'] = "DISTANCE"
        print(data)
    else:
        if data['command'] == '/lowprice':
            data['sort'] = "PRICE_LOW_TO_HIGH"
            print(data)
        elif data['command'] == '/highprice':
            data['sort'] = "PRICE_HIGH_TO_LOW"
            print(data)



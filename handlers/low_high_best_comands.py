from loader import bot
from telebot.types import Message
from loguru import logger
import datetime
from states.user_inputs import UserInputState
from api.first_request import find_destination
from keyboards.inline import city_buttons


@bot.message_handler(commands=['lowprice', 'highprice', 'bestdeal'])
def low_high_best_handler(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInputState.command, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data.clear()
        logger.info('Запоминаем выбранную команду: ' + message.text)
        data['command'] = message.text
        data['date_time'] = datetime.datetime.utcnow().strftime('%d.%m.%Y %H:%M:%S')
        data['telegram_id'] = message.from_user.id
        data['chat_id'] = message.chat.id
    bot.set_state(message.from_user.id, UserInputState.input_city, message.chat.id)
    bot.send_message(message.from_user.id, "Введите город в котором нужно найти отель: ")


@bot.message_handler(state=UserInputState.input_city)
def input_city(message: Message) -> None:
    """
        Здесь пользователь вводит название интересующего его города, который бот запоминает и
        отправляет сообщение функцию find_city(message), проверить наличие города
        :param message:
    """
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['input_city'] = message.text
        logger.info('Пользователь ввел город: ' + message.text)
        region_ids = find_destination(message.text)
        city_buttons.show_cities_buttons(message, region_ids)


def input_quantity(message, temp):
    bot.set_state(message.from_user.id, UserInputState.quantity, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data = temp
        print(data)


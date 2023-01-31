from loader import bot
from telebot.types import Message
from loguru import logger
import datetime
from states.user_inputs import UserInputState
import keyboards.inline
import api
from keyboards.calendar.telebot_calendar import Calendar


def check_command(command):
    if command == '/bestdeal':
        return 'DISTANCE'
    elif command == '/lowprice':
        return 'PRICE_LOW_TO_HIGH'
    elif command == '/highprice':
        return 'PRICE_HIGH_TO_LOW'


@bot.message_handler(state=UserInputState.landmarkIn)
def input_landmark_in(message):
    if message.text.isdigit():
        with bot.retrieve_data(message.chat.id) as data:
            data['landmark_in'] = message.text
        bot.set_state(message.chat.id, UserInputState.landmarkOut)
        bot.send_message(message.chat.id, 'Введите конец диапазона расстояния от центра (км).')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(state=UserInputState.landmarkOut)
def input_landmark_out(message):
    if message.text.isdigit():
        with bot.retrieve_data(message.chat.id) as data:
            data['landmark_out'] = message.text
            print_data(message, data)
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(commands=['lowprice', 'highprice', 'bestdeal'])
def low_high_best_handler(message: Message) -> None:

    my_calendar(message, 'test_calendar')
    bot.set_state(message.chat.id, UserInputState.command)
    with bot.retrieve_data(message.chat.id) as data:
        data.clear()
        logger.info('Запоминаем выбранную команду: ' + message.text)
        data['command'] = message.text
        data['sort'] = check_command(message.text)
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
        region_ids = api.first_request.find_destination(message.text)
        keyboards.inline.city_buttons.show_cities_buttons(message, region_ids)


@bot.message_handler(state=UserInputState.quantity_hotels)
def input_quantity(message):
    if message.text.isdigit():
        if 0 < int(message.text) < 25:
            logger.info('Ввод и запись количества отелей: ' + message.text)
            with bot.retrieve_data(message.chat.id) as data:
                data['quantity_hotels'] = message.text
            bot.set_state(message.chat.id, UserInputState.priceMin)
            bot.send_message(message.chat.id, 'Введите минимальную стоимость отеля:')
        else:
            bot.send_message(message.chat.id, 'Ошибка! Это должно быть число в диапазоне от 1 до 25! Повторите ввод!')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(state=UserInputState.priceMin)
def input_price_min(message):
    if message.text.isdigit():
        logger.info('Ввод и запись минимальной стоимости отеля: ' + message.text)
        with bot.retrieve_data(message.chat.id) as data:
            data['price_min'] = message.text
        bot.set_state(message.chat.id, UserInputState.priceMax)
        bot.send_message(message.chat.id, 'Введите максимальную стоимость отеля:')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(state=UserInputState.priceMax)
def input_price_max(message):
    if message.text.isdigit():
        logger.info('Ввод и запись максимальной стоимости отеля, сравнение с price_min: ' + message.text)
        with bot.retrieve_data(message.chat.id) as data:
            if int(data['price_min']) < int(message.text):
                data['price_max'] = message.text
                keyboards.inline.photo_need.show_buttons_photo_need_yes_no(message)
            else:
                bot.send_message(message.chat.id, 'Максимальная цена должна быть больше минимальной. Повторите ввод!')

    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


@bot.message_handler(state=UserInputState.photo_count)
def input_photo_quantity(message):
    if message.text.isdigit():
        if 1 < int(message.text) < 10:
            logger.info('Ввод и запись количества фотографий: ' + message.text)
            with bot.retrieve_data(message.chat.id) as data:
                data['photo_count'] = message.text
            my_calendar(message, 'заезда')

        else:
            bot.send_message(message.chat.id, 'Число фотографий должно быть в диапазоне от 1 до 10! Повторите ввод!')
    else:
        bot.send_message(message.chat.id, 'Ошибка! Вы ввели не число! Повторите ввод!')


def print_data(message, data):
    print(data)
    bot.send_message(message.chat.id, 'Проверим правильность введённых данных:\n'
                                      f'Дата и время запроса: {data["date_time"]}\n'
                                      f'Введена команда: {data["command"]}\n'
                                      f'Вы ввели город: {data["input_city"]}\n'
                                      f'Выбран город с id: {data["destination_id"]}\n'
                                      f'Количество отелей: {data["quantity_hotels"]}\n'
                                      f'Минимальный ценник: {data["price_min"]}\n'
                                      f'Максимальный ценник: {data["price_max"]}\n'
                                      f'Нужны ли фотографии? {data["photo_need"]}\n'
                                      f'Количество фотографий: {data["photo_count"]}\n'
                                      f'Дата заезда: {data["checkInDate"]["day"]}"-"'
                                      f'{data["checkInDate"]["month"]}"-"{data["checkInDate"]["year"]}\n' 
                                      f'Дата выезда: {data["checkOutDate"]["day"]}"-"'
                                      f'{data["checkInDate"]["month"]}"-"{data["checkInDate"]["year"]}\n'
                     )
    payload = {
        "currency": "USD",
        "eapid": 1,
        "locale": "en_US",
        "siteId": 300000001,
        "destination": {"regionId": data['destination_id']},
        "checkInDate": data['checkInDate'],
        "checkOutDate": data['checkOutDate'],
        "rooms": [
            {
                "adults": 2,
                "children": [{"age": 5}, {"age": 7}]
            }
        ],
        "resultsStartingIndex": 0,
        "resultsSize": int(data["quantity_hotels"]),
        "sort": data['sort'],
        "filters": {"price": {
            "max": data['price_max'],
            "min": data['price_min']
        }}
    }


bot_calendar = Calendar()


def my_calendar(message: Message, word):
    bot.send_message(message.chat.id, f'Выберите дату: {word}',
                     reply_markup=bot_calendar.create_calendar(), )


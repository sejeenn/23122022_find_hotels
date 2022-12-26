from loader import bot
from loguru import logger
import datetime
from states.user_inputs import UserInputState
from keyboards.calendar import calendar
from telebot_calendar import CallbackData
from handlers.low_high_best_comands import print_data

calendar_1_callback = CallbackData("calendar_1", "action", "year", "month", "day")


@bot.callback_query_handler(func=lambda call: call.data.startswith(calendar_1_callback.prefix))
def input_date(call):
    name, action, year, month, day = call.data.split(calendar_1_callback.sep)
    now = datetime.datetime.now().strftime('%Y%m%d')
    select_date = year + month + day
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.set_state(call.message.chat.id, UserInputState.input_date)
    with bot.retrieve_data(call.message.chat.id) as data:
        if 'checkInDate' in data:
            checkin = int(data['checkInDate']['year'] + data['checkInDate']['month'] + data['checkInDate']['day'])
            if int(select_date) > checkin:
                logger.info('Ввод и сохранение даты выезда.')
                data['checkOutDate'] = {'day': day, 'month': month, 'year': year}
                if data['sort'] == 'DISTANCE':
                    bot.set_state(call.message.chat.id, UserInputState.landmarkIn)
                    bot.send_message(call.message.chat.id, 'Введите начало диапазона расстояния от центра (км).')
                else:
                    print_data(call.message, data)
            else:
                bot.send_message(call.message.chat.id, 'Дата выезда должна быть больше даты заезда! '
                                                       'Повторите выбор даты!')
                calendar.my_calendar(call.message, 'выезда')
        else:
            if int(select_date) >= int(now):
                logger.info('Ввод и сохранение даты заезда.')
                data['checkInDate'] = {'day': day, 'month': month, 'year': year}
                calendar.my_calendar(call.message, 'выезда')
            else:
                bot.send_message(call.message.chat.id, 'Дата заезда должна быть больше или равна сегодняшней дате!'
                                                       'Повторите выбор даты!')
                calendar.my_calendar(call.message, 'заезда')


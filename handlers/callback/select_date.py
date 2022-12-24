import handlers.low_high_best_comands
from loader import bot
from loguru import logger
import datetime
from states.user_inputs import UserInputState
from keyboards.calendar import calendar
from telebot_calendar import CallbackData

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
                logger.info('Input checkOutDate')
                data['checkOutDate'] = {'day': day, 'month': month, 'year': year}
                handlers.low_high_best_comands.check_command(call.message, data)
            else:
                bot.send_message(call.message.chat.id, 'CheckOut must be more checkin')
                calendar.my_calendar(call.message)
        else:
            if int(select_date) >= int(now):
                logger.info('Input checkInDate')
                data['checkInDate'] = {'day': day, 'month': month, 'year': year}
                calendar.my_calendar(call.message)
            else:
                bot.send_message(call.message.chat.id, 'CheckIn must be more or equal today date')
                calendar.my_calendar(call.message)


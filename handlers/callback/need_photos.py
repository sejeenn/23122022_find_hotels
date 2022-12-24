from loader import bot
from telebot.types import Message
from loguru import logger
from states.user_inputs import UserInputState
from keyboards.calendar import calendar


@bot.callback_query_handler(func=lambda call: call.data.isalpha())
def need_photo_callback(call) -> None:
    if call.data == 'yes':
        with bot.retrieve_data(call.message.chat.id) as data:
            data['photo_need'] = call.data
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.set_state(call.message.chat.id, UserInputState.photo_count)
        bot.send_message(call.message.chat.id, 'How many photos to show? From 1 to 10')
    elif call.data == 'no':
        with bot.retrieve_data(call.message.chat.id) as data:
            data['photo_need'] = call.data
            data['photo_count'] = '0'
        bot.delete_message(call.message.chat.id, call.message.message_id)
        calendar.my_calendar(call.message)


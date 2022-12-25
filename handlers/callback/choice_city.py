from loader import bot
from telebot.types import Message
from loguru import logger
from states.user_inputs import UserInputState
from handlers import low_high_best_comands


@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def destination_id_callback(call) -> None:
    """
    """
    if call.data:
        bot.set_state(call.message.chat.id, UserInputState.destinationId)
        with bot.retrieve_data(call.message.chat.id) as data:
            data['destination_id'] = call.data
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.set_state(call.message.chat.id, UserInputState.quantity_hotels)
        bot.send_message(call.message.chat.id, 'Сколько вывести отелей? Не более 25!')
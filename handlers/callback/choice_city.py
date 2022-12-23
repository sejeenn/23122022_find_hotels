from loader import bot
from telebot.types import Message
from loguru import logger
from states.user_inputs import UserInputState
from handlers import low_high_best_comands


@bot.callback_query_handler(func=lambda call: call.data.isdigit())
def callback_query(call) -> None:
    """
    """
    if call.data:
        bot.set_state(call.message.from_user.id, UserInputState.destinationId, call.message.chat.id)
        with bot.retrieve_data(call.message.from_user.id, call.message.chat.id) as data:
            data['destination_id'] = call.data
        bot.delete_message(call.message.chat.id, call.message.message_id)
        low_high_best_comands.input_quantity(call.message, data)

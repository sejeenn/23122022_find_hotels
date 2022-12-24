from loader import bot
from telebot import types
from loguru import logger


def show_buttons_photo_need_yes_no(message):
    logger.info('The output of buttons about the need for photos')
    keyboard_yes_no = types.InlineKeyboardMarkup()
    keyboard_yes_no.add(types.InlineKeyboardButton(text='YES', callback_data='yes'))
    keyboard_yes_no.add(types.InlineKeyboardButton(text='NO', callback_data='no'))
    bot.send_message(message.chat.id, "You need photos?", reply_markup=keyboard_yes_no)

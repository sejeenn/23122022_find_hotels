from loader import bot
from telebot.types import Message
from keyboards.calendar.telebot_calendar import Calendar

calendar = Calendar()


def my_calendar(message: Message, word):
    bot.send_message(message.chat.id, f'Выберите дату: {word}',
                     reply_markup=calendar.create_calendar(),
                     )

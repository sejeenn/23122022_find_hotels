from loader import bot
from telebot.types import Message
import datetime
from keyboards.calendar.telebot_calendar import Calendar, CallbackData, RUSSIAN_LANGUAGE

calendar = Calendar()
calendar_1_callback = CallbackData("calendar_1", "action", "year", "month", "day")


def my_calendar(message: Message, word):
    now = datetime.datetime.now()
    bot.send_message(message.chat.id, f'Выберите дату: {word}', reply_markup=calendar.create_calendar(
        name=calendar_1_callback.prefix,
        year=now.year,
        month=now.month,
    ),
                     )

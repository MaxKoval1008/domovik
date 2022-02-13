from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_0 = KeyboardButton('Зарегистрировать заявку на помощь')
button_1 = KeyboardButton('Зарегистрироваться как помощник')

markup_main = ReplyKeyboardMarkup(
    row_width=1,
    resize_keyboard=True,
    one_time_keyboard=False
    ).row(button_0, button_1)

button_start = InlineKeyboardButton('Начать', callback_data='start')
markup_start = InlineKeyboardMarkup(row_width=1).insert(button_start)

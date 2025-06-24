from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboard_start = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Давай!"),
        KeyboardButton(text="Че-то не хочу пока")
    ]], resize_keyboard=True, one_time_keyboard=True
)

keyboard_game = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Камень"),
        KeyboardButton(text="Ножницы"),
        KeyboardButton(text="Бумага")
    ]], resize_keyboard=True
)
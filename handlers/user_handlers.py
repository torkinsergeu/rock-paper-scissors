from aiogram.types import Message, ReplyKeyboardRemove
from aiogram import Router, F
from aiogram.filters import Command

from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import keyboard_start, keyboard_game
from handlers.some_funcs import register_user
from fake_db.users import users_dict

router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer(f"{LEXICON_RU["start"]}", reply_markup=keyboard_start)
    
@router.message(F.text == "Давай!")
async def play(message: Message):
    await message.answer("Отлично!", reply_markup=ReplyKeyboardRemove())
    register_user(message)
    await message.answer("Я загадал!", reply_markup=keyboard_game)    

@router.message(F.text == "Че-то не хочу пока")
async def no(message: Message):
    if message.from_user.id in users_dict.keys() and users_dict[message.from_user.id]:
        await message.answer("Доиграй сначала :)", reply_markup=keyboard_game)
    else:
        await message.answer("Хорошо. Как захочешь - пиши")
@router.message(F.text)
async def in_game(message: Message):
    if message.from_user.id in users_dict.keys() and users_dict[message.from_user.id]:
        user_move = message.text
        robot_move = users_dict[message.from_user.id]
        if (user_move == "Камень" and robot_move == "Бумага" or 
            user_move == "Бумага" and robot_move == "Ножницы" or
            user_move == "Ножницы" and robot_move == "Бумага"):
            users_dict[message.from_user.id] = None
            await message.answer("Я выиграл! Сыграем еще?", reply_markup=keyboard_start)
        elif (user_move == "Камень" and robot_move == "Ножницы" or
              user_move == "Ножницы" and robot_move == "Бумага" or
              user_move == "Бумага" and robot_move == "Камень"):
            users_dict[message.from_user.id] = None
            await message.answer("Ты выиграл! Сыграем еще?", reply_markup=keyboard_start)
        elif user_move == robot_move:
            users_dict[message.from_user.id] = None
            await message.answer("Ничья! Сыграем еще?", reply_markup=keyboard_start)
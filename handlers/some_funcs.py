from aiogram.types import Message
from fake_db.users import users_dict
from random import randint

def register_user(message: Message):
    if message.from_user.id not in users_dict.keys():
        users_dict[message.from_user.id] = [0]*4
    x = randint(1, 3)
    if x == 1:
        robot_move = "Камень"
    elif x == 2:
        robot_move = "Ножницы"
    elif x == 3:
        robot_move = "Бумага"    
    users_dict[message.from_user.id][3] = robot_move

    


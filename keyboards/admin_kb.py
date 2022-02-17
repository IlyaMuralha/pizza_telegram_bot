"""модуль для создания текстовых кнопок интерфейса админа"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

load_btn = KeyboardButton('/Загрузить')
delete_btn = KeyboardButton('/Удалить')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.add(load_btn).add(delete_btn)

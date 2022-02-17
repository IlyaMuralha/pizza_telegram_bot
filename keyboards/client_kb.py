"""модуль для создания текстовых кнопок интерфейса клиента"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# создаём кнопку
b1 = KeyboardButton('/Расположение')
b2 = KeyboardButton('/Режим_работы')
b3 = KeyboardButton('/Меню')
# # атрибут даёт возможность поделиться номером телефона (не работает в десктоп-версии)
# b4 = KeyboardButton('/Поделиться номером', request_contact=True)
# # атрибут даёт возможность поделиться местоположением (не работает в десктоп-версии)
# b5 = KeyboardButton('/Показать где я', request_location=True)

# создаём объект клавиатуры
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
# метод добавляет кнопку в отдельную строку
kb_client.add(b3)
# # метод создает строку с неким количеством кнопок
# kb_client.row(b1, b2)
# метод добавляет кнопку в текущую строку, если есть место
kb_client.add(b1).insert(b2)

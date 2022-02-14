import os
# импортируем модуль emoji для отображения эмоджи
from emoji.core import emojize
from environs import Env

env = Env()
env.read_env()

# Тут у нас будет список из админов
ADMINS = env.list("ADMINS")
# Тоже str, но для айпи адреса хоста
IP = env.str("IP")
# токен выдается при регистрации приложения
# Забираем значение типа str
TOKEN = env.str("BOT_TOKEN")
# название БД
NAME_DB = 'products.db'
# версия приложения
VERSION = '0.0.1'
# автор приложния
AUTHOR = 'Muralha'

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'SEMIPRODUCT': emojize(':pizza: Полуфабрикаты'),
    'GROCERY': emojize(':bread: Бакалея'),
    'ICE_CREAM': emojize(':shaved_ice: Мороженое'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('✅ ЗАКАЗ'),
    'X': emojize('❌'),
    'DOWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
    'COPY': '©️'
}
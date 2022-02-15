import string, json

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import settings.config

token = settings.config.TOKEN

bot = Bot(token=token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен')


'''***********************клиентская часть*********************************'''


@dp.message_handler(commands=['start', 'help'])
async def on_start(message: types.Message):
    """
    функция обрабатывает входящие сообщения при нажатии на команду start or help
    """
    try:
        await bot.send_message(message.from_user.id, f'Приятного аппетита, {message.from_user.first_name}!')
        await message.delete()
    except:
        await message.reply('Для общения с ботом напишите ему в ЛС: \nhttps://t.me/PizzaMuralhaBot')


@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 22:00')


@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пицерийная, 18а')


'''***********************серверная часть**********************************'''
'''***********************общая часть*************************************'''


@dp.message_handler()
async def echo_cenz(message: types.Message):
    """
    функция обрабатывает входящие сообщения не указаных команд, а также фильтрует от мата
    """
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()} \
            .intersection(set(json.load(open('settings/cenz.json')))):
        await message.reply('Мат запрещен!')
        await message.delete()
    else:
        await bot.send_message(message.from_user.id, f'{message.text}: Простите, но я не знаю данной команды. '
                                                     f'Выберете команду из списка')


# @dp.message_handler()
# async def echo_send(message: types.Message):
#     """
#     функция обрабатывает входящие сообщения не указаных команд
#     """
#     # # отвечает сообщением там где получает входящее сообщение
#     # await message.answer(message.text)
#     # # отвечает сообщением пересылая исходное сообщение
#     # await message.reply(message.text)
#     # отправляет сообщения в личку пользователю
#     await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

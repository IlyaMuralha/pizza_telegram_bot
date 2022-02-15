import json
import string

from aiogram import types

from loader import dp, bot


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

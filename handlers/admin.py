"""модуль для админ-панели в телеграм с машиной состояний"""
import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup

from data_base import sqlite_db
from keyboards import kb_admin
from loader import dp, bot
from settings.config import ADMINS

ID = None


class FSMAdmin(StatesGroup):
    """
    класс создает запоминающиеся состояния наследуясь от базового класса
    """
    # запоминаем нужные состояния инициализируя объект класса State
    photo = State()
    name = State()
    description = State()
    price = State()


# проверяем если ID пользователя в списке админов
@dp.message_handler(commands=['Moderator'], is_chat_admin=True)
async def make_changes_commends(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что хозяин надо?', reply_markup=kb_admin)
    await message.delete()


@dp.message_handler(commands='Загрузить')
async def load_start(message: types.Message):
    """
    обработчик запускает диалог загрузки товара в меню бота
    """
    # проверяем является ли юзер админом
    if message.from_user.id == ID:
        # ставим первое состояние в режим ожидания
        await FSMAdmin.first()
        await message.reply('Загрузи фото')


@dp.message_handler(state='*', commands='отмена')
# декоратор с помощью фильтра Text отлавливает совпадения в тексте сообщения
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_load(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ok')


@dp.message_handler(state=FSMAdmin.photo, content_types=['photo'])
async def load_photo(message: types.Message, state: FSMContext):
    """
    обработчик ловит первый ответ и пишет в словарь
    """
    print(message)
    # сохраняем фото из сообщения в словарь data
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    print(message.photo[0].file_id)
    # фиксируем первое состояние и переходим в следующее
    await FSMAdmin.next()
    await message.reply('Теперь введи название')


@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    # сохраняем имя из сообщения в словарь data
    async with state.proxy() as data:
        data['name'] = message.text
    # фиксируем состояние и переходим в следующее
    await FSMAdmin.next()
    await message.reply('Теперь введи описание')


@dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    # фиксируем состояние и переходим в следующее
    await FSMAdmin.next()
    await message.reply('Теперь введи цену товара')


@dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
    # # пока нет базы можно вывести админу или сохранить в файл
    # async with state.proxy() as data:
    #     await message.reply(str(data))
    await sqlite_db.sql_add_command(state)
    logging.debug('Данные сохранены в меню')

    await state.finish()

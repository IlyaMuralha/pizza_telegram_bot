from aiogram import types

from loader import dp, bot


@dp.message_handler(commands=['start', 'help'])
async def on_start(message: types.Message):
    """
    функция обрабатывает входящие сообщения при нажатии на команду start or help
    """
    try:
        await bot.send_message(message.from_user.id, f'Приятного аппетита, {message.from_user.first_name}!')
        # await message.delete()
    except:
        await message.reply('Для общения с ботом напишите ему в ЛС: \nhttps://t.me/PizzaMuralhaBot')


@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 22:00')


@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пицерийная, 18а')

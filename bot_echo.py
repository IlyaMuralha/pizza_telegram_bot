from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import settings.config
token = settings.config.TOKEN

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo_send(message: types.Message):
    # await message.answer(message.text)
    # await message.reply(message.text)
    # отправляет сообщения в личку пользователю
    await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

import settings.config

token = settings.config.TOKEN
bot = Bot(token=token)
dp = Dispatcher(bot)

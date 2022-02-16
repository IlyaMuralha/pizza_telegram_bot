from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import settings.config

storage = MemoryStorage()

token = settings.config.TOKEN
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)

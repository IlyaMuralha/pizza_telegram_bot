from aiogram.utils import executor
import handlers
from data_base import sqlite_db
from loader import dp


async def on_startup(_):
    print('Бот запущен')
    sqlite_db.sql_start()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

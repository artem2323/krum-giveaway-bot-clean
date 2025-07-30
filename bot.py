import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

# Создаем бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("👑 Вы администратор!\n\n"
                             "Этот бот работает!\n\n"
                             "Теперь можно добавлять функционал.")
    else:
        await message.answer("Привет! Этот бот работает!")

# Запуск бота
if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot, skip_updates=True))
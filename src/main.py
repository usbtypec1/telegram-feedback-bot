import pathlib

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor

from handlers import register_handlers

from config import load_config


def main():
    config_file_path = pathlib.Path(__file__).parent.parent / 'config.json'
    config = load_config(config_file_path)

    bot = Bot(config.bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot)

    register_handlers(dp)

    executor.start_polling(dispatcher=dp, skip_updates=True)


if __name__ == '__main__':
    main()

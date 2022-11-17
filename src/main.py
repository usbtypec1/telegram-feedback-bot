import pathlib

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor

from handlers import register_handlers
from middlewares import ConfigInjectMiddleware
from config import load_config
from filters import IsChatIDAllowed, IsChatIDInMessageTextFilter, IsReplyToMessageFilter


def main():
    config_file_path = pathlib.Path(__file__).parent.parent / 'config.json'
    config = load_config(config_file_path)

    bot = Bot(config.bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot)

    dp.setup_middleware(ConfigInjectMiddleware(config))

    filters = {
        'is_admin': IsChatIDAllowed(config.bot.admin_ids),
        'is_chat_id_in_message_text': IsChatIDInMessageTextFilter(),
        'is_reply_to_message': IsReplyToMessageFilter(),
    }

    register_handlers(dp, filters=filters)

    executor.start_polling(dispatcher=dp, skip_updates=True)


if __name__ == '__main__':
    main()

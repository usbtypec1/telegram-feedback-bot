import pathlib

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor

from bot import AdminsBot
from handlers import register_handlers
from middlewares import DependencyInjectMiddleware
from config import load_config
from filters import (
    IsChatIDAllowedFilter,
    IsChatIDInMessageTextFilter,
    IsReplyToMessageFilter,
    IsMessageTextLengthAllowedFilter,
)


def main():
    config_file_path = pathlib.Path(__file__).parent.parent / 'config.json'
    config = load_config(config_file_path)

    bot = Bot(config.bot.token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot)

    admins_bot = AdminsBot(bot, config.bot.admin_ids)

    dp.setup_middleware(DependencyInjectMiddleware(admins_bot=admins_bot, start_message=config.bot.start_message))

    filters = {
        'is_admin': IsChatIDAllowedFilter(config.bot.admin_ids),
        'is_chat_id_in_message_text': IsChatIDInMessageTextFilter(),
        'is_reply_to_message': IsReplyToMessageFilter(),
        'is_message_text_length_allowed': IsMessageTextLengthAllowedFilter(config.bot.message_text_length_limit),
        'is_message_caption_length_allowed': IsMessageTextLengthAllowedFilter(config.bot.message_caption_length_limit),
    }

    register_handlers(dp, filters=filters)

    executor.start_polling(dispatcher=dp, skip_updates=True)


if __name__ == '__main__':
    main()

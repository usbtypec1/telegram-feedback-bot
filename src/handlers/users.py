from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, ContentType

from config import Config
from shortcuts import send_signed_text_message

__all__ = ('register_handlers',)


async def on_start(message: Message, config: Config):
    await message.answer(config.bot.start_message)


async def on_user_text_message(message: Message, config: Config):
    await send_signed_text_message(message.bot, message.text, message.chat.id, config.bot.admin_ids)


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(
        on_start,
        CommandStart(),
    )
    dispatcher.register_message_handler(
        on_user_text_message,
        content_types=(ContentType.TEXT,),
    )

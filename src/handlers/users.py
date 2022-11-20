from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, ContentType

from bot import AdminsBot
from shortcuts import MessageSignature

__all__ = ('register_handlers',)


async def on_start(message: Message, start_message: str):
    await message.answer(start_message)


async def on_user_text_message(message: Message, admins_bot: AdminsBot):
    signature = MessageSignature(chat_id=message.chat.id, message_id=message.message_id)
    await admins_bot.send_messages(message.text, signature)


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_message_handler(
        on_start,
        CommandStart(),
    )
    dispatcher.register_message_handler(
        on_user_text_message,
        content_types=(ContentType.TEXT,),
    )

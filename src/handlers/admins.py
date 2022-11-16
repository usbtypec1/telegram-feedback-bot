from aiogram import Dispatcher

from aiogram.types import Message, ContentType, Update

import exceptions
from shortcuts import extract_chat_id_from_text

__all__ = ('register_handlers',)


async def on_chat_id_not_found_in_message_error(update: Update, exception):
    await update.message.reply('ID пользователя не найдено')
    return True


async def on_admin_message_text(message: Message):
    if message.reply_to_message is None:
        return
    to_chat_id = extract_chat_id_from_text(message.reply_to_message.text)
    await message.bot.send_message(to_chat_id, message.text)


def register_handlers(dispatcher: Dispatcher):
    dispatcher.register_errors_handler(
        on_chat_id_not_found_in_message_error,
        exception=exceptions.ChatIDNotFoundInMessageError,
    )
    dispatcher.register_message_handler(
        on_admin_message_text,
        content_types=(ContentType.TEXT,)
    )

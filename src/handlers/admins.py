from aiogram import Dispatcher
from aiogram.types import Message, ContentType
from aiogram.utils.exceptions import BadRequest

from shortcuts import MessageSignature

__all__ = ('register_handlers',)


async def on_chat_id_not_in_message_text(message: Message):
    await message.reply('ID пользователя не найдено в сообщении')


async def on_admin_message_text(message: Message, message_signature: MessageSignature):
    try:
        await message.bot.send_message(
            chat_id=message_signature.chat_id,
            text=message.text,
            reply_to_message_id=message_signature.message_id,
        )
    except BadRequest:
        await message.reply(f'Не удалось отправить сообщение пользователю с ID{message_signature.chat_id}')


async def on_admin_did_not_reply_to_message(message: Message):
    await message.reply('❗️ Чтобы ответить пользователю, вам нужно именно <b>ответить</b> на сообщение'
                        ', где в конце есть строчка <code>#ID12345678</code>')


def register_handlers(dispatcher: Dispatcher, filters: dict):
    dispatcher.register_message_handler(
        on_admin_did_not_reply_to_message,
        filters['is_admin'],
        ~filters['is_reply_to_message'],
        content_types=ContentType.TEXT,
    )
    dispatcher.register_message_handler(
        on_chat_id_not_in_message_text,
        filters['is_admin'],
        ~filters['is_chat_id_in_message_text'],
        content_types=ContentType.TEXT,
    )
    dispatcher.register_message_handler(
        on_admin_message_text,
        filters['is_admin'],
        filters['is_chat_id_in_message_text'],
        content_types=ContentType.TEXT,
    )

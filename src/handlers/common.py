from aiogram import Dispatcher
from aiogram.types import Message, ContentType


async def on_message_text_length_limit(message: Message):
    await message.reply('Вы превысили лимит по количеству символов в тексте')


def register_handlers(dispatcher: Dispatcher, filters: dict):
    dispatcher.register_message_handler(
        on_message_text_length_limit,
        ~filters['is_message_text_length_allowed'],
        content_types=ContentType.TEXT,
    )
    dispatcher.register_message_handler(
        on_message_text_length_limit,
        ~filters['is_message_caption_length_allowed'],
        content_types=(
            ContentType.PHOTO,
            ContentType.VIDEO,
            ContentType.AUDIO,
            ContentType.DOCUMENT,
            ContentType.VOICE,
        ),
    )

import logging
from typing import Iterable

from aiogram import Bot
from aiogram.utils.exceptions import TelegramAPIError

import exceptions

__all__ = (
    'send_signed_text_message',
    'extract_chat_id_from_text',
)


def extract_chat_id_from_text(text: str) -> int:
    try:
        chat_id = text.split('#ID')[-1]
        return int(chat_id)
    except (ValueError, IndexError):
        raise exceptions.ChatIDNotFoundInMessageError


async def send_signed_text_message(bot: Bot, text: str, from_chat_id: int, to_chat_ids: Iterable[int]):
    text = f'{text}\n\n#ID{from_chat_id}'
    for to_chat_id in to_chat_ids:
        try:
            await bot.send_message(to_chat_id, text)
        except TelegramAPIError:
            logging.warning(f'Could not send message to {to_chat_id}')

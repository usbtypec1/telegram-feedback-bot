import logging
from dataclasses import dataclass
from typing import Iterable

from aiogram import Bot
from aiogram.types import Message, CallbackQuery, Update
from aiogram.utils.exceptions import TelegramAPIError

import exceptions

__all__ = (
    'send_signed_text_message',
    'MessageSignature',
    'get_message',
)


@dataclass(frozen=True, slots=True)
class MessageSignature:
    chat_id: int
    message_id: int

    def to_text(self) -> str:
        return f'#ID{self.chat_id}@{self.message_id}'

    @classmethod
    def from_text(cls, text: str) -> 'MessageSignature':
        try:
            signature_part = text.split('#ID')[-1]
            chat_id, message_id = signature_part.split('@')
            return cls(chat_id=int(chat_id), message_id=int(message_id))
        except (ValueError, IndexError):
            raise exceptions.InvalidSignatureError


def sign_text(signature: MessageSignature, text: str):
    return f'{text}\n\n{signature.to_text()}'


async def send_signed_text_message(
        bot: Bot, text: str,
        message_signature: MessageSignature,
        to_chat_ids: Iterable[int],
):
    signed_text = sign_text(message_signature, text)

    for to_chat_id in to_chat_ids:
        try:
            await bot.send_message(to_chat_id, signed_text)
        except TelegramAPIError:
            logging.warning(f'Could not send message to {to_chat_id}')


def get_message(query: Message | CallbackQuery | Update) -> Message:
    match query:
        case Message():
            return query
        case Update() if query.callback_query is not None:
            return query.callback_query.message
        case CallbackQuery() | Update() if query.message is not None:
            return query.message
        case _:
            raise ValueError('Query must be Message, CallbackQuery or Update type')

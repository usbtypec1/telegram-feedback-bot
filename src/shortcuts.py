from dataclasses import dataclass

from aiogram.types import Message, CallbackQuery, Update

import exceptions

__all__ = (
    'MessageSignature',
    'get_message',
    'sign_text',
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

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

import exceptions
from shortcuts import MessageSignature

__all__ = ('IsChatIDInMessageTextFilter',)


class IsChatIDInMessageTextFilter(BoundFilter):
    key = 'is_chat_id_in_message_text'

    async def check(self, message: Message) -> bool | dict:
        try:
            return {'message_signature': MessageSignature.from_text(message.reply_to_message.text)}
        except exceptions.InvalidSignatureError:
            return False

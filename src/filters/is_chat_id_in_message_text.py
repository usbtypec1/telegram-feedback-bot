from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

import exceptions
from shortcuts import MessageSignature

__all__ = ('IsChatIDInMessageTextFilter',)


class IsChatIDInMessageTextFilter(BoundFilter):
    key = 'is_chat_id_in_message_text'

    async def check(self, message: Message) -> bool | dict:
        message_text = message.reply_to_message.text or message.reply_to_message.caption
        if message_text is None:
            return False
        try:
            return {'message_signature': MessageSignature.from_text(message_text)}
        except exceptions.InvalidSignatureError:
            return False

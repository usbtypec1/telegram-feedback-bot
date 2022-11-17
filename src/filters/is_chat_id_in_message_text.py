from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

import exceptions
from shortcuts import extract_chat_id_from_text

__all__ = ('IsChatIDInMessageTextFilter',)


class IsChatIDInMessageTextFilter(BoundFilter):
    key = 'is_chat_id_in_message_text'

    async def check(self, message: Message) -> bool | dict:
        try:
            return {'from_chat_id': extract_chat_id_from_text(message.reply_to_message.text)}
        except exceptions.ChatIDNotFoundInMessageError:
            return False

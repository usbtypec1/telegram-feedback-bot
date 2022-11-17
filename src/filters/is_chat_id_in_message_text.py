from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

import exceptions
from shortcuts import extract_chat_id_from_text

__all__ = ('IsChatIDInMessageTextFilter',)


class IsChatIDInMessageTextFilter(BoundFilter):
    key = 'chat_ids_filter'

    async def check(self, message: Message) -> bool | dict:
        try:
            return {'from_chat_id': extract_chat_id_from_text(message.text)}
        except exceptions.ChatIDNotFoundInMessageError:
            return False

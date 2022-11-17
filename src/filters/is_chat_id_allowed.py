from typing import Iterable

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery, Update

from shortcuts import get_message

__all__ = ('IsChatIDAllowed',)


class IsChatIDAllowed(BoundFilter):
    key = 'is_chat_id_allowed'

    def __init__(self, chat_ids: Iterable[int]):
        self.__chat_ids = set(chat_ids)

    async def check(self, query: Message | CallbackQuery | Update) -> bool:
        message = get_message(query)
        return message.chat.id in self.__chat_ids

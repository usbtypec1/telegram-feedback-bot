from typing import Iterable

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery, Update

from shortcuts import get_message

__all__ = ('IsChatIDAllowedFilter',)


class IsChatIDAllowedFilter(BoundFilter):
    key = 'is_chat_id_allowed'

    def __init__(self, chat_ids: Iterable[int]):
        self.__chat_ids = set(chat_ids)
        self.__validate_chat_ids()

    def __validate_chat_ids(self):
        if not self.__chat_ids:
            raise ValueError('Chat ids are not provided')

    async def check(self, query: Message | CallbackQuery | Update) -> bool:
        message = get_message(query)
        return message.chat.id in self.__chat_ids

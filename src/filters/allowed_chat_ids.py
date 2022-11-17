from typing import Iterable

from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery, Update

from shortcuts import get_message

__all__ = ('AllowedChatIdsFilter',)


class AllowedChatIdsFilter(BoundFilter):
    key = 'chat_ids_filter'

    def __init__(self, chat_ids: Iterable[int]):
        self.__chat_ids = set(chat_ids)

    async def check(self, query: Message | CallbackQuery | Update) -> bool:
        message = get_message(query)
        return message.chat.id in self.__chat_ids

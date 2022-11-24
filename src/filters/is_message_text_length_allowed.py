from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

__all__ = ('IsMessageTextLengthAllowedFilter',)


class IsMessageTextLengthAllowedFilter(BoundFilter):
    key = 'message_text_limit'

    __slots__ = ('text_length_limit',)

    def __init__(self, text_length_limit: int):
        self.__text_length_limit = text_length_limit

    async def check(self, message: Message) -> bool:
        return len(message.text) < self.__text_length_limit

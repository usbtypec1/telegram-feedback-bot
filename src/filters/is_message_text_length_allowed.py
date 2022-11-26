from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

__all__ = ('IsMessageTextLengthAllowedFilter',)


class IsMessageTextLengthAllowedFilter(BoundFilter):
    key = 'message_text_limit'

    __slots__ = ('text_length_limit',)

    def __init__(self, text_length_limit: int):
        self.__text_length_limit = text_length_limit
        self.__validate_text_length_limit()

    def __validate_text_length_limit(self):
        if self.__text_length_limit <= 1:
            raise ValueError('Length limit must be greater than 1')

    async def check(self, message: Message) -> bool:
        message_text = message.text or message.caption or ''
        return len(message_text) < self.__text_length_limit

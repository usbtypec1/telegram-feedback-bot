from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

__all__ = ('IsMessageTextLengthAllowedFilter',)


class IsMessageTextLengthAllowedFilter(BoundFilter):
    key = 'message_text_limit'

    __slots__ = ('text_length_limit', '__is_message_text_required')

    def __init__(self, text_length_limit: int, *, is_message_text_required: bool = False):
        self.__text_length_limit = text_length_limit
        self.__is_message_text_required = is_message_text_required
        self.__validate_text_length_limit()

    def __validate_text_length_limit(self):
        if self.__text_length_limit <= 1:
            raise ValueError('Length limit must be greater than 1')

    async def check(self, message: Message) -> bool:
        message_text = message.text or message.caption
        if message_text is None:
            return not self.__is_message_text_required
        return len(message_text) < self.__text_length_limit

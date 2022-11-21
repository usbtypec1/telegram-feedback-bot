from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message

__all__ = ('IsReplyToMessageFilter',)


class IsReplyToMessageFilter(BoundFilter):
    key = 'is_reply_to_message'

    async def check(self, message: Message) -> bool:
        return isinstance(message.reply_to_message, Message)

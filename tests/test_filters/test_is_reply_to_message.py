import pytest

from aiogram.types import Message, CallbackQuery

from filters.is_reply_to_message import IsReplyToMessageFilter


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'reply_to_message,expected',
    [
        (Message(), True),
        (CallbackQuery(), False),
        (None, False),
        (1, False),
        ('', False),
        ([], False),
    ]
)
async def test_is_reply_to_message_filter(reply_to_message, expected):
    assert await IsReplyToMessageFilter().check(Message(reply_to_message=reply_to_message)) == expected

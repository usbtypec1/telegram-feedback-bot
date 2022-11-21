import pytest
from aiogram.types import Message

from filters.is_chat_id_in_message_text import IsChatIDInMessageTextFilter
from shortcuts import MessageSignature


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'text,expected',
    [
        ('hello\n#ID876543@12', {'message_signature': MessageSignature(chat_id=876543, message_id=12)}),
        ('hello\n#ID123456@43', {'message_signature': MessageSignature(chat_id=123456, message_id=43)}),
        ('hello\n#ID123456', False),
        ('hello\n#123456', False),
        ('123456', False),
    ]
)
async def test_is_chat_id_in_message_text(text, expected):
    assert await IsChatIDInMessageTextFilter().check(Message(reply_to_message=Message(text=text))) == expected

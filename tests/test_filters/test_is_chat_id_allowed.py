import pytest
from aiogram.types import Message, Chat

from filters.is_chat_id_allowed import IsChatIDAllowedFilter


@pytest.fixture
def message():
    return Message(chat=Chat(id=12345678))


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'allowed_chat_ids,expected',
    [
        ((146546323,), False),
        ((12345678,), True),
        ((12345678, 146546323), True),
    ]
)
async def test_is_chat_id_allowed_filter(message, allowed_chat_ids, expected):
    assert await IsChatIDAllowedFilter(allowed_chat_ids).check(message) == expected


def test_no_allowed_chat_ids_provided(message):
    empty_collections = (tuple(), list(), set(), dict(), frozenset(), str())
    for empty_collection in empty_collections:
        with pytest.raises(ValueError) as error:
            IsChatIDAllowedFilter(empty_collection)
        assert error.value.args[0] == 'Chat ids are not provided'

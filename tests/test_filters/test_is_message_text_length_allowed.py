import pytest
from aiogram.types import Message

from filters.is_message_text_length_allowed import IsMessageTextLengthAllowedFilter


@pytest.fixture
def filter():
    return


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'text,text_length_limit,expected',
    [
        ('aaaaaaaaa', 10, True),
        ('aaaaaaaaaa', 10, False),
        ('aaaaaaaaaaa', 10, False),
        ('bbbbbbbbbbbbbbbbbbbbbbbb', 25, True),
        ('bbbbbbbbbbbbbbbbbbbbbbbbb', 25, False),
        ('bbbbbbbbbbbbbbbbbbbbbbbbbb', 25, False),
    ]
)
async def test_is_message_text_length_allowed(text, text_length_limit, expected):
    filter = IsMessageTextLengthAllowedFilter(text_length_limit)
    assert await filter.check(Message(text=text)) == expected


def test_invalid_message_text_length():
    for text_length_limit in (0, 1):
        with pytest.raises(ValueError) as error:
            IsMessageTextLengthAllowedFilter(text_length_limit)
        assert error.value.args[0] == 'Length limit must be greater than 1'

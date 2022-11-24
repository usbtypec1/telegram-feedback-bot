import pytest
from aiogram.types import Message, CallbackQuery, Update

from shortcuts import get_message


@pytest.mark.parametrize(
    'query',
    [
        Message(),
        Update(callback_query=CallbackQuery(message=Message())),
        Update(message=Message()),
        CallbackQuery(message=Message()),
    ]
)
def test_get_message(query):
    assert isinstance(get_message(query), Message)


@pytest.mark.parametrize(
    'query',
    [
        CallbackQuery(),
        Update(),
        None,
        'fisdfjsdifksdf',
        5345345,
    ]
)
def test_no_message(query):
    with pytest.raises(ValueError) as error:
        get_message(query)
    assert error.value.args[0] == 'Query must be Message, CallbackQuery or Update type'

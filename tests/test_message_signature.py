import pytest

from shortcuts import MessageSignature, sign_text
from exceptions import InvalidSignatureError


@pytest.mark.parametrize(
    'message_signature,expected',
    [
        (MessageSignature(chat_id=1234, message_id=5678), '#ID1234@5678'),
        (MessageSignature(chat_id=534685462, message_id=7865425), '#ID534685462@7865425'),
        (MessageSignature(chat_id=-100423432123, message_id=23425), '#ID-100423432123@23425'),
    ]
)
def test_message_signature_to_text(message_signature, expected):
    assert message_signature.to_text() == expected


@pytest.mark.parametrize(
    'text,expected',
    [
        ('hello\n\n#ID5234236@243', MessageSignature(chat_id=5234236, message_id=243)),
        ('hello\n\n#ID-10025234236@1463', MessageSignature(chat_id=-10025234236, message_id=1463)),
    ]
)
def test_message_signature_from_text(text, expected):
    assert MessageSignature.from_text(text) == expected


@pytest.mark.parametrize(
    'text',
    [
        'hello\n\n#ID324324@',
        'hello\n\n#ID@434',
        'hello\n\n#4234@434',
        'hello\n\n#fsdfs234324@434',
        'hello\n\n#fsdfs234324@43fsd4',
        'hello\n\n#fsdgdfg@asdasf',
        'hello\n\n#fsdgdfg@asdasf',
    ]
)
def test_invalid_message_signature_in_text(text):
    with pytest.raises(InvalidSignatureError):
        MessageSignature.from_text(text)


@pytest.mark.parametrize(
    'message_signature,text,expected',
    [
        (MessageSignature(chat_id=64564563, message_id=456), 'hello', 'hello\n\n#ID64564563@456'),
        (MessageSignature(chat_id=-10053464325, message_id=645645), 'world', 'world\n\n#ID-10053464325@645645'),
    ]
)
def test_sing_text(message_signature, text, expected):
    assert sign_text(message_signature, text) == expected

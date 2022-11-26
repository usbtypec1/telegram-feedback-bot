import logging
from typing import Iterable

from aiogram import Bot
from aiogram.utils.exceptions import TelegramAPIError

from shortcuts import MessageSignature, sign_text


class AdminsBot:
    __slots__ = ('__bot', '__admin_chat_ids')

    def __init__(self, bot: Bot, admin_chat_ids: Iterable[int]):
        self.__bot = bot
        self.__admin_chat_ids = set(admin_chat_ids)

    async def send_messages(self, text: str, message_signature: MessageSignature):
        signed_text = sign_text(message_signature, text)
        for chat_id in self.__admin_chat_ids:
            try:
                await self.__bot.send_message(chat_id, signed_text)
            except TelegramAPIError:
                logging.warning(f'Could not send message to {chat_id}')

    async def send_photos(self, file_id: str, message_signature: MessageSignature, caption: str | None = None):
        caption = caption or ''
        signed_caption = sign_text(message_signature, caption)
        for chat_id in self.__admin_chat_ids:
            try:
                await self.__bot.send_photo(chat_id, file_id, signed_caption)
            except TelegramAPIError:
                logging.warning(f'Could not send photo to {chat_id}')

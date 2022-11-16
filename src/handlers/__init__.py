from aiogram import Dispatcher

from . import admins, users

__all__ = ('register_handlers',)


def register_handlers(dispatcher: Dispatcher):
    admins.register_handlers(dispatcher)
    users.register_handlers(dispatcher)

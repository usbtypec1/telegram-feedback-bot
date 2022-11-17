from aiogram import Dispatcher

from . import admins, users

__all__ = ('register_handlers',)


def register_handlers(dispatcher: Dispatcher, filters: dict):
    admins.register_handlers(dispatcher, filters)
    users.register_handlers(dispatcher)

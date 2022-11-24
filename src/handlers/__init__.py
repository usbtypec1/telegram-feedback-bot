from aiogram import Dispatcher

from . import admins, users, common

__all__ = ('register_handlers',)


def register_handlers(dispatcher: Dispatcher, filters: dict):
    common.register_handlers(dispatcher, filters)
    admins.register_handlers(dispatcher, filters)
    users.register_handlers(dispatcher)

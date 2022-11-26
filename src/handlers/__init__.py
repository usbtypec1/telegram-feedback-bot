from aiogram import Dispatcher

from . import admins, users, common

__all__ = ('register_handlers',)


def register_handlers(dispatcher: Dispatcher, filters: dict):
    """
    The order is important!
    Register handlers in this order:
    1. `common.py`
    2. `admins.py`
    3. `users.py`
    """
    common.register_handlers(dispatcher, filters)
    admins.register_handlers(dispatcher, filters)
    users.register_handlers(dispatcher)

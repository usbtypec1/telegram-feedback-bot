from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from config import Config

__all__ = ('ConfigInjectMiddleware',)


class ConfigInjectMiddleware(LifetimeControllerMiddleware):
    skip_patterns = ["error", "update"]

    def __init__(self, config: Config):
        super().__init__()
        self.__config = config

    async def pre_process(self, obj, data, *args):
        data["config"] = self.__config

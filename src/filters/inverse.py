from aiogram.dispatcher.filters import BoundFilter

__all__ = ('InverseFilter',)


class InverseFilter(BoundFilter):
    key = 'inverse'

    def __init__(self, bound_filter: BoundFilter):
        self.__bound_filter = bound_filter

    async def check(self, *args) -> bool | dict:
        return not await self.__bound_filter(*args)

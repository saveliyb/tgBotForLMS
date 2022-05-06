from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsAdminFilter(BoundFilter):
    """фидльтр для проверки на админа"""
    key = "is_admin"

    def __init__(self, is_admin):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.is_chat_admin()

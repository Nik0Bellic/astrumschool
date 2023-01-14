from aiogram import Dispatcher
from aiogram.types import Message


async def unknown_command(message: Message):
    await message.answer(f'Такой комманды нет, пожалуйста воспользуйтесь командой /help\n\nВ крайних случаях пишите @')


def register_unknown_command_handler(dp: Dispatcher):
    dp.register_message_handler(unknown_command)
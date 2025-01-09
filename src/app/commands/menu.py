from typing import List

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot) -> None:
    commands: List[BotCommand] = [
        BotCommand(command="start", description="Перезапустить бота"),
        BotCommand(command="info", description="Что умеет этот бот?")
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeDefault()
    )

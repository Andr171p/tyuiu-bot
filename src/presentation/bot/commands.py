from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command="start", description="Перезапустить бота"),
        BotCommand(command="info", description="Что умеет этот бот?"),
        BotCommand(command="subscribe", description="Оповестить об изменениях в рейтинге")
    ]
    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeDefault()
    )

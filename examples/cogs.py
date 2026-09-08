from discord.ext import commands

from structrakit import CogManager


async def load_cogs(bot: commands.Bot) -> None:
    manager = CogManager(
        bot,
        directory="cogs",
        dependencies={"cogs.admin": ["cogs.database"]},
    )
    result = await manager.load_all()
    print(result.console_report())


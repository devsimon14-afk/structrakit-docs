from discord.ext import commands

from structrakit import install_error_handler


def configure(bot: commands.Bot) -> None:
    install_error_handler(bot, production=True)


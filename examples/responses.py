import discord
from discord.ext import commands

from structrakit import respond


async def slash(interaction: discord.Interaction) -> None:
    await interaction.response.defer(ephemeral=True)
    await respond(interaction, "Finished.")


async def classic(ctx: commands.Context) -> None:
    await respond(ctx, "Hello from a classic command.")


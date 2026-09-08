import os

import discord
from discord.ext import commands

from structrakit import GuildDatabase, SetupWizard

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)
database = GuildDatabase("data/welcome.db")

wizard = SetupWizard(name="welcome", title="Join/leave setup", database=database)
wizard.add_channel(key="join_channel", label="Join channel", required=True)
wizard.add_channel(key="leave_channel", label="Leave channel")
wizard.add_boolean(key="enabled", label="Enabled", default=True)
wizard.add_text(
    key="join_message",
    label="Join message",
    default="Welcome {member} to {guild}!",
    max_length=1000,
)
wizard.add_text(
    key="leave_message",
    label="Leave message",
    default="{member} left {guild}.",
    max_length=1000,
)


@bot.event
async def setup_hook() -> None:
    await database.connect()


@bot.tree.command()
async def welcome_setup(interaction: discord.Interaction) -> None:
    await wizard.start(interaction)


async def channel_for(guild: discord.Guild, key: str) -> discord.TextChannel | None:
    channel_id = await database.guild(guild.id).namespace("welcome").get(key)
    channel = guild.get_channel(channel_id) if isinstance(channel_id, int) else None
    return channel if isinstance(channel, discord.TextChannel) else None


@bot.event
async def on_member_join(member: discord.Member) -> None:
    settings = database.guild(member.guild.id).namespace("welcome")
    if not await settings.get("enabled", False):
        return
    channel = await channel_for(member.guild, "join_channel")
    template = await settings.get("join_message", "Welcome {member} to {guild}!")
    if channel is not None and isinstance(template, str):
        await channel.send(template.format(member=member.mention, guild=member.guild.name))


@bot.event
async def on_member_remove(member: discord.Member) -> None:
    settings = database.guild(member.guild.id).namespace("welcome")
    if not await settings.get("enabled", False):
        return
    channel = await channel_for(member.guild, "leave_channel")
    template = await settings.get("leave_message", "{member} left {guild}.")
    if channel is not None and isinstance(template, str):
        await channel.send(template.format(member=member.display_name, guild=member.guild.name))


if __name__ == "__main__":
    bot.run(os.environ["DISCORD_TOKEN"])


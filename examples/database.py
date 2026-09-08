from structrakit import GuildDatabase


async def configure(guild_id: int, channel_id: int) -> None:
    async with GuildDatabase("data/settings.db") as database:
        settings = database.guild(guild_id).namespace("welcome")
        await settings.set("enabled", True)
        await settings.set("channel_id", channel_id)
        async with database.transaction() as transaction:
            await transaction.set(guild_id, "welcome", "join", "Welcome!")
            await transaction.set(guild_id, "welcome", "leave", "Goodbye!")


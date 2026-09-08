from discord.ext import commands

from structrakit import Scheduler


async def configure(bot: commands.Bot) -> Scheduler:
    scheduler = Scheduler(bot)

    @scheduler.every(minutes=5)
    async def refresh() -> None:
        return None

    @scheduler.daily(hour=22, timezone="Europe/Berlin")
    async def daily_report() -> None:
        return None

    @scheduler.weekly(weekday="Monday", hour=9, timezone="Europe/Berlin")
    async def weekly_report() -> None:
        return None

    await scheduler.start()
    return scheduler


import discord

from structrakit import diagnose_permissions, require_permissions


@require_permissions(user={"manage_guild": True}, bot={"manage_roles": True})
async def protected(interaction: discord.Interaction) -> None:
    report = diagnose_permissions(
        member=interaction.user if isinstance(interaction.user, discord.Member) else None,
        bot_member=interaction.guild.me if interaction.guild else None,
        channel=interaction.channel,
        required_user_permissions={"manage_guild": True},
        required_bot_permissions={"manage_roles": True},
    )
    print(report.describe())


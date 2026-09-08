import discord

from structrakit import Panel, respond


async def rules(interaction: discord.Interaction, _item: discord.ui.Item) -> None:
    await respond(interaction, "Please read the rules.", ephemeral=True)


panel = (
    Panel(title="Welcome", description="Start here", accent_color=0x57F287)
    .text("Use the controls below.")
    .button(label="Rules", custom_id="welcome:rules", callback=rules)
    .string_select(
        custom_id="welcome:language",
        options=[discord.SelectOption(label="English", value="en")],
    )
)


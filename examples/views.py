import discord

from structrakit import SafeView


class PersistentHelp(SafeView):
    def __init__(self) -> None:
        super().__init__(timeout=None)
        self.add_item(
            discord.ui.ActionRow(discord.ui.Button(label="Help", custom_id="help:open:v1"))
        )


def register(bot: discord.Client) -> None:
    view = PersistentHelp()
    view.validate_persistence()
    bot.add_view(view)


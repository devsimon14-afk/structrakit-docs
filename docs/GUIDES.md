# Guides and examples

Every snippet targets StructraKit 0.1.0 with discord.py 2.7.1 or newer in the 2.x line.

## Slash and classic commands

```python
@bot.tree.command()
async def slash_ping(interaction: discord.Interaction) -> None:
    await respond(interaction, "Pong", ephemeral=True)


@bot.command()
async def prefix_ping(ctx: commands.Context) -> None:
    await respond(ctx, "Pong")
```

## Components V2

Build text, a thumbnail, buttons, and selects with `Panel`. Do not pass classic content or embeds
alongside the returned LayoutView.

```python
async def clicked(interaction: discord.Interaction, item: discord.ui.Item) -> None:
    await respond(interaction, f"Clicked {item.custom_id}", ephemeral=True)


panel = (
    Panel(title="Team", description="Choose an action", accent_color=0x5865F2)
    .thumbnail("https://example.com/team.png")
    .text("Controls are visible below.")
    .button(label="Refresh", custom_id="team:refresh", callback=clicked)
    .role_select(custom_id="team:role", placeholder="Choose a role")
)
await respond(interaction, view=panel.build())
```

## Persistent view registration

Use `timeout=None`, stable unique IDs, and `bot.add_view` during setup. Persistence means Discord
can route future component events; it does not keep a stopped bot online.

## Database and transaction

```python
db = GuildDatabase("data/settings.db")
await db.connect()
settings = db.guild(guild_id).namespace("moderation")
await settings.set("log_channel", channel.id)

async with db.transaction() as tx:
    await tx.set(guild_id, "moderation", "enabled", True)
    await tx.set(guild_id, "moderation", "roles", [role.id])
```

Close the database during bot shutdown. Do not store tokens.

## Permission diagnosis

```python
report = diagnose_permissions(
    member=interaction.user,
    bot_member=interaction.guild.me,
    channel=interaction.channel,
    required_user_permissions={"manage_guild": True},
    required_bot_permissions={"manage_roles": True},
)
if not report.valid:
    await respond(interaction, report.describe(), ephemeral=True)
```

## Setup wizard

```python
wizard = SetupWizard(name="welcome", title="Welcome setup", database=db)
wizard.add_channel(key="join_channel", label="Join channel", required=True)
wizard.add_channel(key="leave_channel", label="Leave channel")
wizard.add_role(key="ping_role", label="Ping role")
wizard.add_boolean(key="enabled", label="Enabled", default=True)
wizard.add_text(key="join_message", label="Join message", max_length=1000)
await wizard.start(interaction)
```

The wizard writes nothing before Save. A Cancel or timeout leaves stored values unchanged.

## Error handling

```python
handle = install_error_handler(bot, production=True)
```

Installation is opt-in. Do not pass `overwrite=True` unless replacing a known custom tree handler
is intentional.

## Cog dependencies

```python
manager = CogManager(
    bot,
    directory="cogs",
    dependencies={"cogs.admin": ["cogs.database"]},
)
result = await manager.load_all()
print(result.console_report())
```

No internet code is loaded. The polling watcher is for local development only.

## Scheduler lifecycle

```python
scheduler = Scheduler(bot)


@scheduler.every(seconds=30)
async def refresh_cache() -> None:
    ...


@scheduler.weekly(weekday="Friday", hour=18, timezone="Europe/Berlin")
async def weekly_digest() -> None:
    ...


await scheduler.start()
# Later, in bot shutdown:
await scheduler.shutdown()
```

One job cannot overlap itself. A spring-DST wall time that does not exist advances to the next
valid minute; an ambiguous autumn wall time runs once.


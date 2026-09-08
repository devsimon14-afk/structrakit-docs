# StructraKit documentation

Documentation and examples:  
https://github.com/devsimon14-afk/structrakit-docs

This directory is the publication-ready content for the future public documentation repository.
It contains user documentation and public examples only—no StructraKit implementation source.

StructraKit 0.1.0 is a proprietary, typed, asynchronous toolkit for the original `discord.py`. It
provides safe responses, Components V2 panels, owner-aware views, guild-scoped SQLite settings,
permission checks, setup wizards, error routing, local cog management, and time-zone-aware jobs.

## Install

```console
python -m pip install structrakit
```

Documentation and examples:
https://github.com/devsimon14-afk/structrakit-docs

Supported combinations:

| Python | discord.py | Wheels |
|---|---|---|
| CPython 3.11–3.14 | `>=2.7.1,<3.0` | Windows x86-64, Manylinux x86-64, macOS x86-64/ARM64 |

Detailed platform instructions are in [Installation](docs/INSTALLATION.md). StructraKit ships
binary wheels only; no source distribution is published. The package neither uses a post-install
hook nor prints during import.

## Quick start

```python
import os

import discord
from discord.ext import commands

from structrakit import install_error_handler, respond

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())
install_error_handler(bot)


@bot.tree.command()
async def ping(interaction: discord.Interaction) -> None:
    await respond(interaction, "Pong!", ephemeral=True)


bot.run(os.environ["DISCORD_TOKEN"])
```

Never store the token in source code. Use a bot token, never a user token or selfbot.

## Documentation map

- [Installation on Windows, Linux, and macOS](docs/INSTALLATION.md)
- [Complete public API: every class, function, parameter, and return value](docs/API.md)
- [Guides: commands, Components V2, persistence, database, wizard, permissions, scheduler, and cogs](docs/GUIDES.md)
- [Copy-ready examples for every public module](examples/README.md)
- [Troubleshooting and FAQ](docs/TROUBLESHOOTING.md)
- [Deutsche Dokumentation](README_DE.md)
- [Changelog](CHANGELOG.md)
- [Proprietary license overview](LICENSE_OVERVIEW.md)
- [Security and issue reporting](SUPPORT.md)

## Essential examples

Safe deferred interaction:

```python
@bot.tree.command()
async def save(interaction: discord.Interaction) -> None:
    await interaction.response.defer(ephemeral=True)
    await respond(interaction, "Saved.")
```

Classic command:

```python
@bot.command()
async def hello(ctx: commands.Context) -> None:
    await respond(ctx, "Hello!")
```

Components V2:

```python
panel = (
    Panel(title="Welcome", description="Start here", accent_color=0x57F287)
    .text("Please read the rules.")
    .button(label="Rules", custom_id="welcome:rules")
)
await respond(interaction, view=panel.build())
```

Guild database:

```python
async with GuildDatabase("data/settings.db") as db:
    welcome = db.guild(interaction.guild_id).namespace("welcome")
    await welcome.set("enabled", True)
    enabled = await welcome.get("enabled", False)
```

Permissions:

```python
@bot.tree.command()
@require_permissions(user={"manage_guild": True}, bot={"manage_roles": True})
async def setup(interaction: discord.Interaction) -> None:
    await respond(interaction, "Allowed", ephemeral=True)
```

Scheduler:

```python
scheduler = Scheduler(bot)


@scheduler.daily(hour=22, timezone="Europe/Berlin")
async def report() -> None:
    ...


await scheduler.start()
```

## Package information

```console
structrakit info
python -m structrakit info
```

Expected fields are version, developer, proprietary license, and documentation URL.

## Limits and safety

StructraKit uses public discord.py APIs and does not monkey-patch Discord classes or silently
replace global handlers. Components V2 cannot use classic content and embeds. Persistent views
still require stable IDs and re-registration after restart. Cogs are loaded only from the configured
local directory. SQLite statements are parameterized. Unknown command failures are logged locally
with an error ID; common token forms are removed from exception messages.

Cython compilation keeps normal private implementation `.py` files out of wheels, but compiled
code is not impossible to analyze. This is not a claim of absolute source protection.

## License

StructraKit is proprietary software developed by dev.simon.

You may install and use the unmodified package in your own Discord bots.
You may not modify, sell, repackage, sublicense, or republish StructraKit
as your own package.

Using the unmodified dependency inside a private or public bot, deployment, or Docker container is
permitted. The package itself may not be republished. This is not an open-source license. See
[LICENSE_OVERVIEW.md](LICENSE_OVERVIEW.md) and the `LICENSE` shipped in the package.

## Issues

Report reproducible bugs through [GitHub Issues](https://github.com/devsimon14-afk/structrakit-docs/issues). Include
versions, platform, minimal code, and a sanitized traceback. Never include tokens, credentials,
private repository URLs, or sensitive user data.

Documentation, guides, examples, FAQ, changelog, and issue tracker:  
https://github.com/devsimon14-afk/structrakit-docs

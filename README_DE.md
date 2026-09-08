# StructraKit – Dokumentation

Dokumentation, Anleitungen und Beispiele:  
https://github.com/devsimon14-afk/structrakit-docs

StructraKit 0.1.0 ist eine proprietäre, asynchrone und typisierte Ergänzung für das originale
`discord.py>=2.7.1,<3.0`. Unterstützt werden CPython 3.11–3.14 sowie Wheels für Windows x86-64,
Manylinux x86-64 und macOS x86-64/ARM64.

## Installation

```console
python -m pip install structrakit
```

Dokumentation, Anleitungen und Beispiele:
https://github.com/devsimon14-afk/structrakit-docs

Unter Windows kann `py -m pip install structrakit` verwendet werden. Unter Linux und macOS sollte
zuerst mit `python3 -m venv .venv` eine virtuelle Umgebung erstellt werden. Das Paket enthält keinen
Post-Installations-Hook und schreibt beim Import nichts in die Konsole.

```powershell
structrakit info
py -m structrakit info
```

## Schnellstart

```python
import os
import discord
from discord.ext import commands
from structrakit import respond

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())


@bot.tree.command()
async def ping(interaction: discord.Interaction) -> None:
    await respond(interaction, "Pong!", ephemeral=True)


bot.run(os.environ["DISCORD_TOKEN"])
```

## Inhalte

- [Installation für Windows, Linux und macOS](docs/INSTALLATION.md)
- [Vollständige öffentliche API](docs/API.md)
- [Anleitungen und getestete Modulbeispiele](docs/GUIDES.md)
- [Häufige Fehler und FAQ](docs/TROUBLESHOOTING.md)
- [Changelog](CHANGELOG.md)
- [Lizenzübersicht](LICENSE_OVERVIEW.md)
- [Fehler sicher über GitHub Issues melden](SUPPORT.md)

Die API-Dokumentation beschreibt `respond`, `smart_send`, `Panel`, `SafeView`, `GuildDatabase`,
Transaktionen und Scopes, `require_permissions`, `diagnose_permissions`, `validate_layout`,
`SetupWizard`, `install_error_handler`, `CogManager`, `Scheduler`, alle Parameter, Rückgabewerte,
Exceptions und Ergebnis-Dataclasses. Die Guides enthalten Slash Commands, klassische Commands,
Components V2, persistente Views, Datenbank, Wizard, Berechtigungen, Cogs und Scheduler.

## Wichtige Hinweise

- Components V2 dürfen nicht mit klassischem `content` oder Embeds kombiniert werden.
- Persistente Views benötigen `timeout=None`, stabile IDs und erneute Registrierung beim Start.
- Datenbankzugriffe verwenden parametrisierte Abfragen; Tokens dürfen trotzdem nie gespeichert werden.
- Der CogManager lädt ausschließlich lokale Dateien.
- Der Scheduler verwendet `zoneinfo` und verhindert parallele Doppelausführungen.
- Cython-Binärmodule sind kein absoluter Schutz vor Analyse.

## Lizenz

StructraKit ist proprietäre Software von dev.simon.

Das unveränderte Paket darf kostenlos in eigenen Discord-Bots verwendet
werden. Es darf nicht verändert, verkauft, umbenannt, unterlizenziert oder
als eigenes Paket neu veröffentlicht werden.

Die unveränderte Nutzung als Abhängigkeit in privaten und öffentlichen Bots, Servern oder
Docker-Containern ist erlaubt. Das eigenständige Paket darf nicht neu veröffentlicht werden.
Gesetzlich zwingende Rechte bleiben unberührt. StructraKit ist nicht Open Source; für Abhängigkeiten
wie discord.py gelten deren eigene Lizenzen. Maßgeblich ist die mit dem Paket gelieferte englische
`LICENSE`.

Fehler bitte ohne Tokens oder sensible Daten über
https://github.com/devsimon14-afk/structrakit-docs/issues melden.

Dokumentation, Anleitungen, Beispiele, FAQ und Changelog:  
https://github.com/devsimon14-afk/structrakit-docs


# Troubleshooting and FAQ

## Frequent errors

### No matching distribution found

StructraKit provides wheels only. Use supported CPython and platform versions and update pip. Add
`python --version` and `python -m pip debug -v` to an issue.

### Components V2 conflict

Discord ignores classic content and embeds once the Components V2 message flag is active. Put text
in `TextDisplay` and media in V2 media/file components.

### Database is not connected

Call `await db.connect()` before using scopes, or use `async with GuildDatabase(...) as db`.

### Permission diagnosis says allowed but Discord rejects the operation

Permission state can change, some operations have extra Discord constraints, and role hierarchy
matters. Treat local diagnosis as a preflight, handle `discord.Forbidden`, and avoid assuming a
check guarantees a future request.

### Persistent controls do not work after restart

Re-create a timeout-free view using exactly the same custom IDs and call `bot.add_view(view)` from
`setup_hook`. The original message must still exist.

### Scheduled time behaves differently during DST

Use an IANA zone such as `Europe/Berlin`, not a fixed abbreviation. Nonexistent spring times move
to the next valid minute; ambiguous autumn times run once.

## FAQ

**Which Discord library is supported?** Only the original discord.py 2.7.1 or newer 2.x release.

**Does StructraKit modify discord.py globally?** No monkey-patching is performed.

**Does installation run custom code?** No post-install hook is used.

**Does import print a link?** No. Use `structrakit info` or `python -m structrakit info`.

**Can compiled wheels be reverse-engineered?** Potentially. Cython removes ordinary private source
files from wheels but cannot make code impossible to analyze.

**Can a bot containing StructraKit be deployed publicly?** Yes, if StructraKit remains an
unmodified dependency. Standalone republishing, sale, modification, and sublicensing are restricted
by its proprietary license.

**Where are bugs reported?** https://github.com/devsimon14-afk/structrakit-docs/issues


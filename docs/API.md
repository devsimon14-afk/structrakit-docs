# Complete public API

This reference describes StructraKit 0.1.0. All awaitable results must be awaited.

## Root API

The supported root imports are `respond`, `smart_send`, `Panel`, `SafeView`, `GuildDatabase`,
`DatabaseTransaction`, `GuildScope`, `NamespaceScope`, `require_permissions`,
`diagnose_permissions`, `validate_layout`, `SetupWizard`, `WizardSession`,
`install_error_handler`, `CogManager`, `Scheduler`, the public exception classes, and the public
result dataclasses. `__version__` is a string.

## `responses`

### `respond(target, content=None, **kwargs) -> Any`

Convenience alias for `smart_send`; returns the underlying discord.py response result.

### `smart_send(target, content=None, *, view=None, embed=None, embeds=None, ephemeral=False,
allowed_mentions=None, delete_after=None, file=None, files=None, edit_original=False) -> Any`

- `target`: interaction, command context, or messageable object.
- `content`: classic message text or `None`.
- `view`: native `View` or `LayoutView`.
- `embed`/`embeds`: mutually exclusive single or multiple embeds; at most ten.
- `ephemeral`: interaction-only private response flag.
- `allowed_mentions`: native mention policy.
- `delete_after`: deletion delay supported by the chosen Discord endpoint.
- `file`/`files`: mutually exclusive upload parameters; at most ten.
- `edit_original`: explicitly edit the original interaction response.

Deferred responses edit the original; completed normal responses use follow-up. Raises
`ValidationError` for conflicts and `UnsupportedTargetError` for unsupported targets.

## `ui.Panel`

`Panel(*, title=None, description=None, accent_color=None, timeout=180.0)` requires title or
description. Accent colors are integers from `0x000000` to `0xFFFFFF` or `discord.Colour`.

All builder methods return the panel:

- `thumbnail(media)` accepts URL, Discord file, or `UnfurledMediaItem`.
- `text(content)` accepts 1–4000 Markdown characters.
- `separator(*, visible=True, large=False)` adds spacing.
- `button(*, label, custom_id, emoji=None, style=primary, disabled=False, callback=None)` adds an
  interactive button. Callback receives interaction and item.
- `link_button(*, label, url, emoji=None, disabled=False)` adds a link button.
- `string_select(*, custom_id, options, placeholder=None, min_values=1, max_values=1,
  disabled=False, callback=None)` uses `discord.SelectOption` entries.
- `user_select`, `role_select`, and `mentionable_select` accept `custom_id`, placeholder,
  min/max values, disabled, and callback.
- `channel_select` additionally accepts `channel_types`.
- `component(item)` copies a native discord.py item for each build.
- `build() -> discord.ui.LayoutView` returns a new validated view.

## `views.SafeView`

`SafeView(*, owner_id=None, allowed_user_ids=(), allowed_role_ids=(), timeout=180.0,
disable_on_timeout=True, unauthorized_message=..., error_callback=None)` extends LayoutView.

- `bind_message(message) -> SafeView` enables timeout editing.
- `interaction_check(interaction) -> bool` applies user and role access.
- `on_error(interaction, error, item) -> None` logs and routes callback errors.
- `on_timeout() -> None` optionally disables interactive children.
- `validate_persistence() -> None` requires `timeout=None` and stable IDs or raises
  `ValidationError`.

## `database`

`GuildDatabase(path)` accepts a filesystem path or `:memory:`.

- `connected -> bool`
- `connect() -> GuildDatabase`; creates tables.
- `close() -> None`; idempotent.
- `set(guild_id, namespace, key, value) -> None`
- `get(guild_id, namespace, key, default=None) -> JSONValue`
- `delete(guild_id, namespace, key) -> bool`
- `all(guild_id, namespace) -> dict[str, JSONValue]`
- `delete_namespace(guild_id, namespace) -> int`
- `delete_guild(guild_id) -> int`
- `guild(guild_id) -> GuildScope`
- `transaction()` is an async context manager yielding `DatabaseTransaction`.

`DatabaseTransaction` exposes atomic `set`, `get`, and `delete`. `GuildScope.namespace(name)`
returns `NamespaceScope`; `GuildScope.delete()` removes the guild. `NamespaceScope` exposes
`set`, `get`, `delete`, `all`, and `clear`. JSONValue supports strings, integers, floats, booleans,
null, lists, and dictionaries with string keys. Failures raise `DatabaseError` or
`ConfigurationError`.

## `permissions`

`require_permissions(*, user=None, bot=None, guild_only=True, allow_owner=True)` returns a
decorator usable on slash or classic callbacks. User and bot mappings contain real Discord
permission names and booleans. Failed checks raise `PermissionCheckError`.

`diagnose_permissions(*, member, bot_member, channel, required_user_permissions=None,
required_bot_permissions=None, guild_only=True, target_role=None) -> PermissionReport` checks
effective channel permissions and optional role hierarchy.

`PermissionReport` fields: `guild_only_satisfied`, `missing_user_permissions`,
`missing_bot_permissions`, `role_position_satisfied`, and `reason`; `valid` is derived and
`describe()` returns text.

## `limits`

`validate_layout(view, *, content=None, embed=None, embeds=None, files=None) -> ValidationReport`
checks Components V2 and legacy layout limits plus message compatibility.

`ValidationReport.issues` contains `ValidationIssue(path, message, severity, suggestion)`.
`valid`, `errors`, and `warnings` are derived properties; `add(...)` appends a finding.

## `wizard`

`SetupWizard(*, name, title, database, timeout=300.0)` defines a guild-only wizard.

- `settings -> tuple[WizardSetting, ...]`
- `add_channel`, `add_role`, `add_user`, `add_mentionable`: `key`, `label`, optional `required`,
  integer-ID `default`, and `validator`.
- `add_boolean`: `key`, `label`, boolean `default`, and validator.
- `add_text`: `key`, `label`, optional `required`, string `default`, `max_length` 1–4000, validator.
- `start(interaction, *, ephemeral=True) -> WizardSession`

A validator receives JSONValue and returns an error string or `None`. `WizardSession` exposes
`wizard`, `guild_id`, `owner_id`, `values`, `step`, `completed`, `cancelled`, `timed_out`,
`on_summary`, and `wait() -> dict | None`.

## `errors`

Exception hierarchy: `StructraKitError` → `ConfigurationError`, `DatabaseError`,
`ValidationError`, `PermissionCheckError`, and `UnsupportedTargetError`.

`install_error_handler(bot, *, production=True, logger=None, log_callback=None,
overwrite=False) -> ErrorHandlerHandle` installs one application-command handler and one classic
listener. A log callback receives error ID and sanitized exception and may be sync or async.
`redact_secrets(value) -> str` sanitizes common credential forms.

## `cogs`

`CogManager(bot, directory="cogs", *, package=None, exclude=(), dependencies=None)` uses only
local files.

- `discover() -> tuple[str, ...]`
- `load`, `unload`, `reload` each return `CogLoadResult`.
- `load_all() -> CogBatchResult`
- `start_watcher(*, interval=1.0) -> None`
- `stop_watcher() -> None`

`CogLoadResult` fields are extension, status, error, and dependencies. `CogBatchResult` exposes
results, loaded, skipped, failed, and `console_report()`.

## `scheduler`

`Scheduler(bot, *, error_callback=None, success_store=None, time_source=None, sleep=asyncio.sleep)`
registers async jobs.

- `every(*, seconds=0, minutes=0, hours=0, name=None)`
- `daily(*, hour, minute=0, timezone="UTC", name=None)`
- `weekly(*, weekday, hour, minute=0, timezone="UTC", name=None)`
- `start()`, `run_now(name) -> bool`, `pause(name)`, `resume(name)`, `stop(name)`, and `shutdown()`
- `status(name) -> SchedulerStatus`; `statuses() -> tuple[SchedulerStatus, ...]`
- Async context-manager entry starts and exit shuts down.

Error callback receives job name and exception. Success store receives job name and aware UTC
datetime. Time source must return an aware datetime. `SchedulerStatus` exposes name, running,
paused, next run, last run, last success, and last error.


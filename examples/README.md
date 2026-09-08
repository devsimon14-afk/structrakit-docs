# Tested examples

These examples are syntax-checked in the private release pipeline against the supported API.

- `responses.py`: slash, deferred, and classic responses
- `panels.py`: Components V2 Panel
- `views.py`: persistent SafeView registration
- `database.py`: scopes and atomic transaction
- `permissions.py`: decorator and diagnosis
- `wizard.py`: join/leave SetupWizard definition
- `join_leave_bot.py`: complete join/leave configuration and event listeners
- `errors.py`: opt-in error handler
- `cogs.py`: local dependency-ordered loading
- `scheduler.py`: interval, daily, and weekly jobs

Set `DISCORD_TOKEN` only in the environment for complete bot programs. The snippets intentionally
do not include a token or make a Discord connection on import.

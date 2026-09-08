# Installation

## Supported versions

StructraKit 0.1.0 supports CPython 3.11–3.14 and the original `discord.py>=2.7.1,<3.0`.
Published wheels target Windows x86-64, Manylinux x86-64, macOS x86-64, and macOS ARM64. Python
3.14 remains conditional on compatible discord.py dependencies.

## Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install structrakit
py -m structrakit info
```

If PowerShell blocks activation, the venv can be used without activating it:

```powershell
.\.venv\Scripts\python.exe -m pip install structrakit
.\.venv\Scripts\python.exe -m structrakit info
```

The Windows dependency `tzdata` supplies IANA time zones for `zoneinfo`.

## Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install structrakit
python3 -m structrakit info
```

The official wheel is Manylinux x86-64. Alpine/musl and 32-bit systems are not part of the 0.1.0
matrix.

## macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install structrakit
python3 -m structrakit info
```

Use an ARM64 Python on Apple Silicon to select the ARM64 wheel. Under Rosetta, an x86-64 Python
selects the x86-64 wheel.

## Verify

```console
python -c "import structrakit; print(structrakit.__version__)"
```

Expected: `0.1.0`. Import itself emits no message and performs no network operation.

## No matching distribution

1. Run `python --version`; it must be a supported CPython.
2. Run `python -m pip install --upgrade pip`.
3. Run `python -m pip debug -v` and compare compatible wheel tags.
4. Confirm the OS and architecture appear above.
5. Report the sanitized output at https://github.com/devsimon14-afk/structrakit-docs/issues.

No source distribution exists, so pip will not compile StructraKit on an unsupported platform.


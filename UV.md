# UV

A newer tool, aiming to simplify running python in diverse settings.

* manage python versions
    * alternative to pyenv
* setup project (uv init)
    * manage dependencies
* run a standalone tool (uvx yt-dlp)
* install a standalone tool (uv tool install yt-dlp)

## Setup project

```
$ cd project
$ uv init .
```

Creates:

* python-version
* .pyproject.toml

Example project configuration file.

```
[project]
name = "llm24"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []
```

Add dependency:

```
$ uv add ruff
```

This will automatically add a venv (not activated). It will also add a
lockfile, `uv.lock` listing dependency version and hashes.

Run a command:

```
$ uv run ruff check
```

## Run any standalone tool

```
$ uvx yt-dlp
```

Drop into a ipython shell:

```
$ uvx ipython
```

## Install a tool

```
$ uv tool install ruff
```


## Manage python version

```
$ uv python install 3.10 3.11 3.12
```

Use `--python` on subcommands:

```
$ uv venv --python 3.8.1
```

Or:

```
$ uv run --python 3.8.1 -- python
```

Only run with already installed python versions.

Controlled by `.python-version`, can be set with pin:

```
$ uv python pin 3.8.1
```

## Standalone script support

Add dep to script:

```
$ uv add --script example.py requests
```

Results in:

```
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
# ]
# ///
import requests; print(requests.get("https://heise.de"))
```

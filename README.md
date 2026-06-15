# langchain-class

A LangChain class project, managed with [uv](https://docs.astral.sh/uv/).

The app runs against a **local LM Studio** server by default — no OpenAI API key required.

## Migrated from Pipenv → uv

This project was originally defined by a `Pipfile`. It has been migrated to uv, and
all dependencies were upgraded to their latest releases in the process:

| Package          | Old (Pipfile) | Now       |
| ---------------- | ------------- | --------- |
| langchain        | `0.0.352`     | `1.3.9`   |
| langchain-openai | `0.0.5`       | `1.3.2`   |
| python-dotenv    | `1.0.0`       | `1.2.2`   |
| Python           | `3.11`        | `3.13`    |

The `Pipfile` has been removed; `pyproject.toml` + `uv.lock` are now the single source
of truth.

## Prerequisites

- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed.
  uv manages the Python toolchain itself — it will download Python 3.13 on first use,
  so no system Python is required.
- [LM Studio](https://lmstudio.ai/) running locally with a model loaded and the local
  server enabled (default: `http://localhost:1234/v1`).

## How this project was initialized

The exact steps used to create this project from scratch:

```bash
# 1. Scaffold a uv project targeting Python 3.13 (no VCS side effects).
uv init --python 3.13 --vcs none

# 2. Add the dependencies, unpinned, so uv resolves the latest versions.
#    This writes them into pyproject.toml and locks exact versions in uv.lock.
uv add langchain langchain-openai python-dotenv

# 3. Remove the obsolete Pipenv file.
rm Pipfile
```

Versions in `pyproject.toml` use `>=` specifiers; exact, reproducible versions are
captured in `uv.lock`.

## Project structure

```
main.py            # CLI entry point (argparse)
llm.py             # Creates the ChatOpenAI client pointed at LM Studio
app_modes/
  chatbot.py       # Interactive multi-turn chatbot
  codegen.py       # Generates a function + test via a two-step chain
tests/
  test_cli.py      # Unit tests for the CLI argument parser
```

## Usage

```bash
uv sync              # Create/restore the virtual env from uv.lock
uv run main.py       # Run the default codegen mode (LM Studio on localhost:1234)
uv run main.py --mode chatbot
uv run main.py --mode codegen --task "return a list of numbers" --language python
```

### CLI flags

| Flag          | Default                        | Description                          |
| ------------- | ------------------------------ | ------------------------------------ |
| `--mode`      | `codegen`                      | `codegen` or `chatbot`               |
| `--task`      | `"return a list of numbers"`   | Prompt task for codegen mode         |
| `--language`  | `python`                       | Target language for codegen mode     |
| `--base-url`  | `http://localhost:1234/v1`     | LM Studio (or any OpenAI-compatible) |
| `--api-key`   | `lm-studio`                    | Any non-empty string for LM Studio   |
| `--model`     | `google/gemma-4-e4b`           | Model name as shown in LM Studio     |

### Running tests

```bash
uv run python -m unittest discover -s tests
```

### Other uv commands

```bash
uv add <package>     # Add a new dependency
uv lock --upgrade    # Refresh the lockfile to the latest compatible versions
```

## Note on the langchain upgrade

LangChain jumped from `0.0.x` to the stable `1.x` line, which carries breaking API
changes. Any new code should target the modern langchain 1.x API. Legacy chains and
helpers from the old line now live in the separate `langchain-classic` package.

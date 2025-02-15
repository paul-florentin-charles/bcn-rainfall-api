# bcn-rainfall-api

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![coverage badge](coverage.svg)](https://github.com/nedbat/coveragepy)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

API build with FastAPI to expose rainfall data from the city of Barcelona, Catalunya.


### Requirements

- Python 3.12
- Pip

### Get started


```commandline
git clone https://github.com/paul-florentin-charles/bcn-rainfall-api.git
cd bcn-rainfall-api
pip install uv
uv sync
uv run run.py
```

### Tests & Coverage

```commandline
uv run coverage run -m pytest
uv run coverage report
```

### Code quality

```commandline
uv tool run mypy --check-untyped-defs .
uv tool run ruff check
uv tool run ruff format
```
# Flask CI App

Simple Flask web app with CI pipeline using GitHub Actions.

## Features

- `/` – Home route
- `/status` – Health check
- `/add/<a>/<b>` – Adds two numbers

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Testing
```bash
pytest
```

## Code Quality
```
flake8 .
black --check .
```
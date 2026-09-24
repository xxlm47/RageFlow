# RageFlow AI

Multi-agent social content research and generation pipeline for Facebook.

## Pipeline
Trend Radar → Research → Ideation → Critic → Safety → Optimization → Output → Learning

Designed for Android/Termux with Python + SQLite. AI providers are adapters so RageFlow can use an OpenAI-compatible endpoint, a local model endpoint, or offline development mode.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m rageflow run --topic "relatable everyday arguments"
```

Use `--offline` for zero-API development.

RageFlow is intended for legitimate social publishing. It does not automate fake engagement, coordinated commenting, impersonation, harassment, threats, discriminatory attacks, or platform-enforcement evasion.

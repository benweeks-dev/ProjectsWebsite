# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Copy env template and set SECRET_KEY / RESEND_API_KEY / MAIL_RECIPIENT
cp .env.example .env

# Run development server
python run.py

# Seed database with sample data
python seed_data.py

# Access Flask shell (for database operations)
flask shell

# View submitted contact messages
python messages.py
```

## Architecture

This is a Flask portfolio website using the application factory pattern with Blueprints.

### Entry Points
- `run.py` - Application entry point, runs the dev server
- `app/__init__.py` - App factory (`create_app()`) that initializes extensions and registers blueprints

### Blueprints (in `app/blueprints/`)
| Blueprint | URL Prefix | Purpose |
|-----------|------------|---------|
| `main` | `/` | Home page with featured projects |
| `projects` | `/projects` | Project list and detail views |
| `about` | `/about` | About page with skills |
| `contact` | `/contact` | Contact form (Flask-WTF) |
| `resume` | `/resume` | Resume with experience/education/certifications |

### Database Models (`app/models.py`)
- `Project` - Portfolio projects (title, description, technologies as comma-separated string, github/live URLs)
- `Skill` - Skills with category and proficiency (1-100)
- `Experience` - Work history
- `Education` - Education history
- `ContactMessage` - Submitted contact form messages

Each model has additional bookkeeping fields beyond what's listed above (timestamps, display ordering, location, etc.) - see `app/models.py` for the full schema.

### Configuration
- `config.py` - Flask config (SECRET_KEY, SQLite database URI, Resend mail settings)
- Database file: `app.db` (SQLite, auto-created on first run)
- Email: the contact form always persists to `ContactMessage`. If `RESEND_API_KEY` and `MAIL_RECIPIENT` are set (see `.env.example`), it also sends a notification email via Resend (`app/blueprints/contact.py`); otherwise email sending is silently skipped.

### Deployment
Deployed to Render.com via `render.yaml` (build: `pip install -r requirements.txt && python seed_data.py`, start: `gunicorn run:app`). A `Procfile` is also present for compatibility.

### Templates
Bootstrap 5 templates in `app/templates/`. Base template provides navbar, flash messages, and footer. Project images go in `app/static/images/`.

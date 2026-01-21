# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python run.py

# Seed database with sample data
python seed_data.py

# Access Flask shell (for database operations)
flask shell
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
| `resume` | `/resume` | Resume with experience/education |

### Database Models (`app/models.py`)
- `Project` - Portfolio projects (title, description, technologies as comma-separated string, github/live URLs)
- `Skill` - Skills with category and proficiency (1-100)
- `Experience` - Work history
- `Education` - Education history
- `ContactMessage` - Submitted contact form messages

### Configuration
- `config.py` - Flask config (SECRET_KEY, SQLite database URI)
- Database file: `app.db` (SQLite, auto-created on first run)

### Templates
Bootstrap 5 templates in `app/templates/`. Base template provides navbar, flash messages, and footer. Project images go in `app/static/images/`.

# Portfolio Website

A personal portfolio website built with Flask to showcase programming projects, skills, and professional experience.
Hosted at https://benweeks.dev/ (via render.com)

## Technologies

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite
- **Forms**: Flask-WTF with email validation

## Features

- Project gallery with detail pages
- Skills display with proficiency indicators
- Resume page with work experience and education
- Contact form with validation (SQL and Resend via email)
- Responsive design

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/benweeks-dev/ProjectsWebsite.git
   cd ProjectsWebsite
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

5. Open http://127.0.0.1:5000 in your browser

## Configuration

Copy `.env.example` to `.env` and set:
- `SECRET_KEY` - Flask session secret
- `RESEND_API_KEY` / `MAIL_RECIPIENT` - enables the contact form to send a notification email via [Resend](https://resend.com) when someone submits it

The app runs fine without these — submissions are still saved to the database, the email just won't send.

## Managing Content

Seed the database with sample data:
```bash
python seed_data.py
```

The database (`app.db`) persists on disk. Once seeded, data stays there until you:
- Run `seed_data.py` again (clears and re-adds everything)
- Delete `app.db` manually
- Modify the database via Flask shell

To add or update content later:
1. Edit `seed_data.py` and re-run it (replaces all data), or
2. Use Flask shell to add individual entries without affecting existing ones:
   ```bash
   flask shell
   >>> from app.models import Project
   >>> p = Project(title="My Project", description="Description here", technologies="Python, Flask")
   >>> db.session.add(p)
   >>> db.session.commit()
   ```
3. Eventually build an admin page to add/edit projects through the website

Project screenshots go in `app/static/images/`, referenced from the project's record.

View submitted contact messages:
```bash
python messages.py
```

## Screenshot

<!-- Add a screenshot of site here -->
<!-- ![Screenshot](screenshot.png) -->

## Roadmap

- Unify screenshot framing and make screenshots click through to the project page
- Fix JumpSim web leaderboard

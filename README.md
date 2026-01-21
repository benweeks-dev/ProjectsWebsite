# Portfolio Website

A personal portfolio website built with Flask to showcase programming projects, skills, and professional experience.

## Technologies

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite
- **Forms**: Flask-WTF with email validation

## Features

- Project gallery with detail pages
- Skills display with proficiency indicators
- Resume page with work experience and education
- Contact form with validation
- Responsive design

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/bSlope8348/ProjectsWebsite.git
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

## Adding Content

Seed the database with sample data:
```bash
python seed_data.py
```

Or add content via Flask shell:
```bash
flask shell
>>> from app.models import Project
>>> p = Project(title="My Project", description="Description here", technologies="Python, Flask")
>>> db.session.add(p)
>>> db.session.commit()
```

## Screenshot

<!-- Add a screenshot of your site here -->
<!-- ![Screenshot](screenshot.png) -->

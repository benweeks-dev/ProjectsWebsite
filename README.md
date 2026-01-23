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


## Getting Started (TODOs)

  1. Create a virtual environment and install dependencies:
  
      python -m venv venv
  
      venv\Scripts\activate
  
      pip install -r requirements.txt

  2. Run the app:

      python run.py

  3. Visit http://127.0.0.1:5000 in your browser

  4. (Optional) Add sample data:

      python seed_data.py

  5. Next Steps

  - Add your projects: Use seed_data.py as a template or add via Flask shell:
  flask shell
      - from app.models import Project
      - p = Project(title="My Project", description="...", technologies="Python, Flask")
      - db.session.add(p)
      - db.session.commit()
  - Add project screenshots: Place images in app/static/images/ and reference them in projects

## Updating Projects and Skills in Database

  The database (app.db) persists on disk. Once you seed it, the data stays there until you:
  - Run seed_data.py again (which clears and re-adds everything)
  - Delete app.db manually
  - Modify the database via Flask shell

  So for adding new projects later, you can either:
  1. Edit seed_data.py and re-run it (replaces all data)
  2. Use Flask shell to add individual entries without affecting existing ones
  3. Eventually build an admin page to add/edit projects through the website
"""
Seed script to populate the database with sample data.
Run this after creating the database to see the site with example content.

Usage: python seed_data.py
"""
from datetime import date
from app import create_app, db
from app.models import Project, Skill, Experience, Education

app = create_app()

def seed_database():
    with app.app_context():
        # Clear existing data
        Project.query.delete()
        Skill.query.delete()
        Experience.query.delete()
        Education.query.delete()

        # Add sample projects
        projects = [
            Project(
                title="Portfolio Website",
                description="A personal portfolio website built with Flask and Bootstrap to showcase my projects and skills.",
                long_description="""
                <p>This is a full-stack web application built to showcase my programming projects and professional experience.</p>
                <h5>Features:</h5>
                <ul>
                    <li>Responsive design using Bootstrap 5</li>
                    <li>SQLite database for storing projects and content</li>
                    <li>Contact form with email validation</li>
                    <li>Dynamic project gallery</li>
                </ul>
                """,
                technologies="Python, Flask, SQLite, Bootstrap, HTML, CSS",
                github_url="https://github.com/yourusername/portfolio",
                featured=True,
                date_completed=date(2024, 1, 15)
            ),
            Project(
                title="Task Manager App",
                description="A simple task management application with user authentication and CRUD operations.",
                technologies="Python, Flask, SQLAlchemy, JavaScript",
                github_url="https://github.com/yourusername/task-manager",
                featured=True,
                date_completed=date(2023, 11, 20)
            ),
            Project(
                title="Weather Dashboard",
                description="A weather dashboard that fetches data from an API and displays forecasts with charts.",
                technologies="Python, Flask, API Integration, Chart.js",
                github_url="https://github.com/yourusername/weather-dashboard",
                live_url="https://weather-demo.example.com",
                featured=True,
                date_completed=date(2023, 9, 10)
            ),
        ]

        # Add sample skills
        skills = [
            Skill(name="Python", category="Languages", proficiency=85),
            Skill(name="JavaScript", category="Languages", proficiency=70),
            Skill(name="HTML/CSS", category="Languages", proficiency=80),
            Skill(name="SQL", category="Languages", proficiency=75),
            Skill(name="Flask", category="Frameworks", proficiency=80),
            Skill(name="Bootstrap", category="Frameworks", proficiency=85),
            Skill(name="SQLAlchemy", category="Frameworks", proficiency=70),
            Skill(name="Git", category="Tools", proficiency=75),
            Skill(name="VS Code", category="Tools", proficiency=90),
            Skill(name="Docker", category="Tools", proficiency=50),
        ]

        # Add sample experience
        experiences = [
            Experience(
                title="Junior Developer",
                company="Tech Company Inc.",
                location="Remote",
                start_date=date(2023, 6, 1),
                is_current=True,
                description="Developing web applications using Python and Flask. Collaborating with team members on various projects."
            ),
            Experience(
                title="Intern",
                company="Startup XYZ",
                location="City, State",
                start_date=date(2023, 1, 1),
                end_date=date(2023, 5, 31),
                description="Assisted in building internal tools and learned best practices for software development."
            ),
        ]

        # Add sample education
        education = [
            Education(
                degree="Bachelor of Science in Computer Science",
                institution="University Name",
                location="City, State",
                start_date=date(2019, 9, 1),
                end_date=date(2023, 5, 15),
                gpa="3.5",
                description="Relevant coursework: Data Structures, Algorithms, Web Development, Database Systems"
            ),
        ]

        # Add all to database
        db.session.add_all(projects)
        db.session.add_all(skills)
        db.session.add_all(experiences)
        db.session.add_all(education)
        db.session.commit()

        print("Database seeded successfully!")
        print(f"Added {len(projects)} projects")
        print(f"Added {len(skills)} skills")
        print(f"Added {len(experiences)} experiences")
        print(f"Added {len(education)} education entries")


if __name__ == "__main__":
    seed_database()

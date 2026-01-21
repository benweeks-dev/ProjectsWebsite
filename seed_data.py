"""
Seed script to populate the database with projects and other data.
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

        # Add projects
        projects = [
            Project(
                title="Portfolio Website",
                description="A personal portfolio website built with Flask and Bootstrap to showcase my projects, skills, and professional experience.",
                long_description="""
                <p>A full-stack web application built to showcase my programming projects and professional experience.</p>
                <h5>Features:</h5>
                <ul>
                    <li>Responsive design using Bootstrap 5</li>
                    <li>SQLite database with SQLAlchemy ORM</li>
                    <li>Flask Blueprints for modular architecture</li>
                    <li>Contact form with Flask-WTF validation</li>
                    <li>Dynamic project gallery with detail pages</li>
                    <li>Resume page with experience and education sections</li>
                </ul>
                <h5>What I Learned:</h5>
                <ul>
                    <li>Flask application factory pattern</li>
                    <li>Database modeling with SQLAlchemy</li>
                    <li>Form handling and validation</li>
                    <li>Template inheritance with Jinja2</li>
                </ul>
                """,
                technologies="Python, Flask, SQLAlchemy, SQLite, Bootstrap, HTML, CSS",
                github_url="https://github.com/bSlope8348/ProjectsWebsite",
                image_filename="portfolio-screenshot.png",  # Add your screenshot filename here
                featured=True,
                date_completed=date(2026, 1, 20)
            ),
            Project(
                title="JumpSim",
                description="A 2D platformer game built with LÖVE2D and Lua, featuring SQLite leaderboards and physics-based gameplay.",
                long_description="""
                <p>A 2D platformer game created as my CS50 final project to learn Lua, game development, and database integration.</p>
                <h5>Game Links:</h5>
                <ul>
                    <li><a href="https://bslope8348.github.io/cs50_final_project" target="_blank" rel="noopener">Play JumpSim in a Browser</a></li>
                    <p>Controls: Left/Right arrow keys to move, Space to jump, Esc for menu.<br>
                    Note: SQL is not currently supported for the web build so the leaderboard will be empty.</p>
                    <li><a href="https://github.com/bSlope8348/cs50_final_project/releases" target="_blank" rel="noopener">Downloadable Builds for Windows/Mac</a></li>
                    <p>Note: Will need to download .zip file, unzip the entire folder, then run JumpSim.exe or JumpSim.love</p>
                </ul>
                <h5>Features:</h5>
                <ul>
                    <li>Two playable characters collecting coins and reaching exits</li>
                    <li>Physics-based collision system with walls, platforms, and movable boxes</li>
                    <li>SQLite3 local leaderboard tracking top 10 completion times</li>
                    <li>Save/load game functionality</li>
                    <li>Built-in timer and pause menu</li>
                    <li>SQL injection protection for user input</li>
                </ul>
                <h5>What I Learned:</h5>
                <ul>
                    <li>Lua programming and LÖVE2D game framework</li>
                    <li>2D game physics and collision detection</li>
                    <li>Integrating SQLite databases in games</li>
                    <li>Cross-platform builds (Windows, macOS, Linux, Web)</li>
                </ul>
                """,
                technologies="Lua, LÖVE2D, SQLite3, Visual Studio Code",
                github_url="https://github.com/bSlope8348/cs50_final_project",
                image_filename="jumpsim-screenshot.png",
                featured=True,
                date_completed=date(2025, 11, 21)
            ),
        ]

        # Add skills (adjust proficiency levels as needed)
        skills = [
            Skill(name="Python", category="Languages", proficiency=80),
            Skill(name="JavaScript", category="Languages", proficiency=60),
            Skill(name="HTML/CSS", category="Languages", proficiency=75),
            Skill(name="SQL", category="Languages", proficiency=70),
            Skill(name="C", category="Languages", proficiency=65),
            Skill(name="C++", category="Languages", proficiency=60),
            Skill(name="Lua", category="Languages", proficiency=50),
            Skill(name="MATLAB", category="Languages", proficiency=55),
            Skill(name="Visual Basic", category="Languages", proficiency=50),
            Skill(name="Flask", category="Frameworks", proficiency=75),
            Skill(name="Bootstrap", category="Frameworks", proficiency=70),
            Skill(name="SQLAlchemy", category="Frameworks", proficiency=65),
            Skill(name="Git", category="Tools", proficiency=70),
            Skill(name="VS Code", category="Tools", proficiency=85),
        ]

        # Add experience (customize with your own)
        experiences = [
            # Example:
            # Experience(
            #     title="Software Developer",
            #     company="Company Name",
            #     location="Denver, CO",
            #     start_date=date(2023, 6, 1),
            #     is_current=True,
            #     description="Description of your role and accomplishments."
            # ),
        ]

        # Add education (customize with your own)
        education = [
            # Example:
            # Education(
            #     degree="Bachelor of Science in Computer Science",
            #     institution="University Name",
            #     location="City, State",
            #     start_date=date(2019, 9, 1),
            #     end_date=date(2023, 5, 15),
            #     gpa="3.5",
            #     description="Relevant coursework: ..."
            # ),
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

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
                title="JumpSim",
                description="A 2D platformer game built with LÖVE2D and Lua, featuring SQLite leaderboards and physics-based gameplay.",
                long_description="""
                <p>A 2D platformer game created as my CS50 final project to learn Lua, game development, and database integration.</p>
                <h5>Game Links:</h5>
                <ul>
                    <li><a href="https://benweeks-dev.github.io/cs50_final_project" target="_blank" rel="noopener">Play JumpSim in a Browser</a></li>
                    <p>Controls: Left/Right arrow keys to move, Space to jump, Esc for menu.<br>
                    Note: SQL is not currently supported for the web build so the leaderboard will be empty.</p>
                    <li><a href="https://github.com/benweeks-dev/cs50_final_project/releases" target="_blank" rel="noopener">Downloadable Builds for Windows/Mac</a></li>
                    <p>Note: Download the .zip file, unzip the entire folder, then run JumpSim.exe or JumpSim.love</p>
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
                github_url="https://github.com/benweeks-dev/cs50_final_project",
                image_filename="jumpsim-screenshot.png",
                featured=True,
                display_order=1,
                date_completed=date(2025, 11, 21)
            ),
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
                github_url="https://github.com/benweeks-dev/ProjectsWebsite",
                image_filename="portfolio-screenshot.png",
                featured=True,
                display_order=2,
                date_completed=date(2026, 1, 20)
            ),
            Project(
                title="XML Merger",
                description="A project to merge two or more XML files (e.g. gamelist.xml) into one comprehensive file.",
                long_description="""
                <p>Complete toolkit for managing and standardizing gamelist.xml files across multiple platforms.</p>
                <h5>Features:</h5>
                <ul>
                    <li><strong>gamelist_unifier.py</strong> - Main library for merging and standardizing gamelists</li>
                    <li><strong>test_ngp.py</strong> - Single system processing example (NGP; edit paths inside to use for other systems)</li>
                    <li><strong>batch_process_custom.py</strong> - Process all systems at once (paths hardcoded inside for pc setup)</li>
                    <li><strong>deploy_unified_gamelists.py</strong> - Copy unified gamelists to Game and PC backup folders</li>
                    <li><strong>gamelist_to_backup.py</strong> - Activate unified gamelists in folders (backs up originals, renames new ones)</li>
                </ul>
                <h5>What I Learned:</h5>
                <ul>
                    <li>How to use Python's Path library and dataclasses</li>
                    <li>Comparing data and keeping the more detailed information</li>
                    <li>Implementing changes to standardize older files</li>
                    <li>Having Claude Code iterate on ideas, but debugging issues on my own when errors occurred or output incorrect.</li>
                </ul>
                """,
                technologies="Python, pathlib, dataclasses, XML(ElementTree)",
                github_url="https://github.com/benweeks-dev/xml_merger",
                image_filename="xml_merger-screenshot.png",
                featured=True,
                display_order=4,
                date_completed=date(2026, 3, 5)
            ),
            Project(
                title="Hangman (Python Implementations)",
                description="A classic Hangman word-guessing game implemented three ways in Python: command-line, Tkinter desktop GUI, and a Flask web app.",
                long_description="""
                <p>A classic word-guessing game built three different ways in Python to compare console, desktop GUI, and web-based approaches to the same core game logic.</p>
                <h5>Implementations:</h5>
                <ul>
                    <li><strong>CLI version</strong> - Terminal-based game with text input and game-state display</li>
                    <li><strong>Tkinter version</strong> - Desktop GUI with on-screen keyboard and visual feedback</li>
                    <li><strong>Flask version</strong> - Browser-playable web app version</li>
                </ul>
                <h5>What I Learned:</h5>
                <ul>
                    <li>Python code written by hand for knowledge base. Claude code used to build frontend for web base app.</li>
                    <li>Separating game logic from the interface so it could be reused across CLI, GUI, and web layers</li>
                    <li>Differences in state management and input handling across console, desktop, and web paradigms</li>
                    <li>Building a minimal Flask app and routes for a simple interactive game</li>
                </ul>
                """,
                technologies="Python, Tkinter, Flask",
                github_url="https://github.com/benweeks-dev/Hangman",
                image_filename="hangman-screenshot.png",
                featured=True,
                display_order=3,
                date_completed=date(2026, 6, 24)
            )
        ]

        # Add skills (proficiency: 1=Learning, 2=Familiar, 3=Proficient, 4=Expert)
        skills = [
            # Languages
            Skill(name="Python", category="Languages", proficiency=4),
            Skill(name="JavaScript", category="Languages", proficiency=2),
            Skill(name="HTML/CSS", category="Languages", proficiency=3),
            Skill(name="SQL", category="Languages", proficiency=2),
            Skill(name="C", category="Languages", proficiency=1),
            Skill(name="C++", category="Languages", proficiency=1),
            Skill(name="Lua", category="Languages", proficiency=2),
            Skill(name="MATLAB", category="Languages", proficiency=3),
            Skill(name="Visual Basic", category="Languages", proficiency=2),
            # Frameworks & Tools
            Skill(name="Flask", category="Frameworks & Tools", proficiency=2),
            Skill(name="Bootstrap", category="Frameworks & Tools", proficiency=2),
            Skill(name="LÖVE2D", category="Frameworks & Tools", proficiency=2),
            Skill(name="Simulink", category="Frameworks & Tools", proficiency=4),
            Skill(name="Git/GitHub", category="Frameworks & Tools", proficiency=3),
            Skill(name="VS Code", category="Frameworks & Tools", proficiency=3),
            # Database
            Skill(name="SQLite3", category="Database", proficiency=3),
            Skill(name="Database Design", category="Database", proficiency=3),
            # Engineering
            Skill(name="Control Systems", category="Engineering", proficiency=4),
            Skill(name="AutoCAD", category="Engineering", proficiency=2),
        ]

        # Add experience
        experiences = [
            Experience(
                title="Engineering Project Lead (Electrical)",
                company="US Bureau of Reclamation, Technical Service Center",
                location="Denver, CO",
                start_date=date(2008, 6, 1),
                end_date=date(2025, 9, 30),
                is_current=False,
                description="Managed six-figure projects from planning through commissioning, serving as client liaison to 5 regional offices. Led team of 6 engineers, managing project budgets and coordinating powerplant personnel/contractors. Successfully commissioned 12+ new digital control systems for hydroelectric generators. Developed efficient compliance testing workflows that reduced testing/generator downtime by 50%. Created comprehensive procedures enabling field personnel to perform routine tests independently, reducing travel costs by 25%. Mentored junior engineers in testing, generator tuning, and project management."
            ),
        ]

        # Add education
        education = [
            Education(
                degree="CS50x: Introduction to Computer Science",
                institution="Harvard University",
                location="Online",
                end_date=date(2025, 11, 1),
                description="Comprehensive computer science fundamentals including algorithms, data structures, memory management, and software engineering principles."
            ),
            Education(
                degree="Bachelor of Science in Electrical Engineering",
                institution="Colorado School of Mines",
                location="Golden, CO",
                end_date=date(2008, 5, 15),
                description="Professional Engineer (PE) License - Colorado State License, Licensed since 2013, Active through October 2027"
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

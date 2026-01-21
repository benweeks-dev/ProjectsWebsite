from app import create_app, db
from app.models import Project, Skill, Experience, Education

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Project': Project,
        'Skill': Skill,
        'Experience': Experience,
        'Education': Education
    }


if __name__ == '__main__':
    app.run(debug=True)

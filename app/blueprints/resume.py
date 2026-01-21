from flask import Blueprint, render_template
from app.models import Experience, Education, Skill

resume_bp = Blueprint('resume', __name__)


@resume_bp.route('/')
def resume():
    experiences = Experience.query.order_by(Experience.start_date.desc()).all()
    education = Education.query.order_by(Education.end_date.desc()).all()
    skills = Skill.query.order_by(Skill.category, Skill.proficiency.desc()).all()

    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        category = skill.category or 'Other'
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)

    return render_template('resume.html',
                         experiences=experiences,
                         education=education,
                         skills_by_category=skills_by_category)

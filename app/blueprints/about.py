from flask import Blueprint, render_template
from app.models import Skill

about_bp = Blueprint('about', __name__)


@about_bp.route('/')
def about():
    skills = Skill.query.order_by(Skill.category, Skill.proficiency.desc()).all()

    # Group skills by category
    skills_by_category = {}
    for skill in skills:
        category = skill.category or 'Other'
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)

    return render_template('about.html', skills_by_category=skills_by_category)

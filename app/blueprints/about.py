from flask import Blueprint, render_template
from app.models import Skill

about_bp = Blueprint('about', __name__)


@about_bp.route('/')
def about():
    skills = Skill.query.order_by(Skill.proficiency.desc()).all()

    # Define category order
    category_order = ['Languages', 'Frameworks & Tools', 'Database', 'Engineering', 'Other']

    # Group skills by category in specified order
    skills_by_category = {cat: [] for cat in category_order}
    for skill in skills:
        category = skill.category or 'Other'
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)

    # Remove empty categories
    skills_by_category = {k: v for k, v in skills_by_category.items() if v}

    return render_template('about.html', skills_by_category=skills_by_category)

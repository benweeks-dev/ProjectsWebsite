from flask import Blueprint, render_template
from app.models import Project

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    featured_projects = Project.query.filter_by(featured=True).limit(3).all()
    return render_template('index.html', projects=featured_projects)

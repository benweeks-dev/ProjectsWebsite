from flask import Blueprint, render_template
from app.models import Project

projects_bp = Blueprint('projects', __name__)


@projects_bp.route('/')
def list_projects():
    projects = Project.query.order_by(Project.date_created.desc()).all()
    return render_template('projects/list.html', projects=projects)


@projects_bp.route('/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('projects/detail.html', project=project)

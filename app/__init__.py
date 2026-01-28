from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    # Register blueprints
    from app.blueprints.main import main_bp
    from app.blueprints.projects import projects_bp
    from app.blueprints.about import about_bp
    from app.blueprints.contact import contact_bp
    from app.blueprints.resume import resume_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(projects_bp, url_prefix='/projects')
    app.register_blueprint(about_bp, url_prefix='/about')
    app.register_blueprint(contact_bp, url_prefix='/contact')
    app.register_blueprint(resume_bp, url_prefix='/resume')

    # Create database tables and seed if empty
    with app.app_context():
        db.create_all()

        from app.models import Project
        if Project.query.first() is None:
            from seed_data import seed_database
            seed_database()

    return app

from datetime import datetime
from app import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    long_description = db.Column(db.Text)
    technologies = db.Column(db.String(200))  # Comma-separated list
    github_url = db.Column(db.String(200))
    live_url = db.Column(db.String(200))
    image_filename = db.Column(db.String(100))
    featured = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_completed = db.Column(db.Date)

    def __repr__(self):
        return f'<Project {self.title}>'

    def get_technologies_list(self):
        if self.technologies:
            return [t.strip() for t in self.technologies.split(',')]
        return []


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50))  # e.g., 'Language', 'Framework', 'Tool'
    proficiency = db.Column(db.Integer)  # 1-100 scale for progress bars

    def __repr__(self):
        return f'<Skill {self.name}>'


class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)  # None means current position
    description = db.Column(db.Text)
    is_current = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Experience {self.title} at {self.company}>'


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(100), nullable=False)
    institution = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.Text)
    gpa = db.Column(db.String(10))

    def __repr__(self):
        return f'<Education {self.degree} from {self.institution}>'


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<ContactMessage from {self.name}>'

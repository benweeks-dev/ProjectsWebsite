import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    _db_url = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # Railway provides postgresql:// but SQLAlchemy requires postgresql+psycopg2://
    SQLALCHEMY_DATABASE_URI = _db_url.replace('postgresql://', 'postgresql+psycopg2://', 1)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail settings
    RESEND_API_KEY = os.environ.get('RESEND_API_KEY')
    MAIL_RECIPIENT = os.environ.get('MAIL_RECIPIENT')

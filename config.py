import os


DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://shorturladmin:23830000@localhost/shorturl_db')


class Config:
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

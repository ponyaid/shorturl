import os


class Config:
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = f'postgresql://shorturladmin:23830000@localhost/shorturl_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

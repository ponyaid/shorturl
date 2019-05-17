from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from flask_login import UserMixin

from app.database import db
from app.login import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    links = db.relationship('Link', backref='user')

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_link = db.Column(db.String)
    page = db.Column(db.String, unique=True)
    short_link = db.Column(db.String)
    visits = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, index=True, default=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<ID {self.id}>'

    def get_date(self):
        return self.created.strftime('%d.%m.%y %H:%M')

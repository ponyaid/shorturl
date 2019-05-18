from flask import Flask

from config import Config
from .database import db
from .login import login


def create_app(config_filename=Config):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    login.init_app(app)

    import app.user.controllers as user
    import app.link.controllers as link

    app.register_blueprint(user.module)
    app.register_blueprint(link.module)

    return app




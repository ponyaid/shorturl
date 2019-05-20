from flask_script import Manager
from flask_migrate import Migrate

from app import create_app
from app.database import db


app = create_app()

manager = Manager(app)
migrate = Migrate(app, db)




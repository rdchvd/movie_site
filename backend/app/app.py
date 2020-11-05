from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


# from flask_security import SQLAlchemyUserDatastore
# from flask_security import Security
# from flask_security import current_user

from flask import redirect, url_for, request

app = Flask(__name__, static_folder="/frontend/static")
app.config.from_object(Configuration)
app.static_folder=app.config.get('STATIC_FOLDER')
app.static_url_path=app.config.get('STATIC_PATH')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

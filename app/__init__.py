from flask import Flask
from flask_login import LoginManager

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

__version__ = '0.1.0'

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)

from app import routes, models

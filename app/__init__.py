from flask import Flask
from config import Config

__version__ = '0.1.0'

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

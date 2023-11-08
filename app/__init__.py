from flask import Flask
from .api.routes import api

from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, ma
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(api)

app.config.from_object(Config)
root_db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)
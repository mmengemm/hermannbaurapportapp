import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
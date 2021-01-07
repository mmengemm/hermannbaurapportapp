import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_session import Session
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = Config.SECRET_KEY
db = SQLAlchemy(app)
db.init_app(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
Talisman(app)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)
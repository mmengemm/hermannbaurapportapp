import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_session import Session
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = Config.SECRET_KEY
db = SQLAlchemy(app)
db.init_app(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
Talisman(app)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
from .admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint)

from .models import User
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
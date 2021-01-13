import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_session import Session
from flask_talisman import Talisman
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_fontawesome import FontAwesome

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = Config.SECRET_KEY
db = SQLAlchemy(app)
db.init_app(app)
fa = FontAwesome(app)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
from .admin import admin
app.register_blueprint(admin.admin)
from application.rapport.rapport import rapportBP as rapport_blueprint
app.register_blueprint(rapport_blueprint)

csrf = CSRFProtect(app)
csrf.init_app(app)
talisman = Talisman(app)
talisman.content_security_policy_report_only = True
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


from .models import User
@login_manager.user_loader
def load_user(id):
    return User.query.filter(User.id == int(id))
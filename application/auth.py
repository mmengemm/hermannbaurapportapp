from flask import Blueprint,render_template
from . import db, app
from .forms import LoginForm

auth = Blueprint('auth', __name__)

@auth.route('/')
def login():
    error = None
    msg = None
    form = LoginForm()
    return render_template('login.html',form=form,msg=msg, error=error)

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'
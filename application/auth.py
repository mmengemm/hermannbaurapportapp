from flask import Blueprint,render_template, request,session
from . import db, app
from .forms import LoginForm
from .db_requests import *
auth = Blueprint('auth', __name__)
import os

@auth.route('/',methods=['GET','POST'])
def login():
    error = None
    msg = None
    form = LoginForm()
    if form.validate_on_submit():
        os.environ['USERNAME'] = form.username.data
        os.environ['PASSWORD'] = form.password.data
        session['username'] = form.username.data
        ui = UserInformation()
        user, error = ui.get_user(os.getenv('USERNAME'),os.getenv('PASSWORD'))
        if user is None:
            error = error
        else:
            session['logged_in'] = True
            admin = user.admin
            if admin:
                pass
            else:
                pass

    return render_template('login.html',form=form,msg=msg, error=error)

@auth.route('/signup')
def signup():
    return 'Signup'

@auth.route('/logout')
def logout():
    return 'Logout'
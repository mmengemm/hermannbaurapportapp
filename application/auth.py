from flask import Blueprint,render_template, request,session,redirect, url_for
from flask_login import login_user,logout_user,login_required, current_user
from . import db, app
from .forms import LoginForm, RegisterForm
from .db_requests import *
auth = Blueprint('auth', __name__)
import os
import re
from .random_string import get_random_string
from flask_hashing import Hashing

hashing = Hashing(app)

@auth.route('/',methods=['GET','POST'])
def login():
    error = None
    msg = None
    form = LoginForm()
    if request.method == 'POST':
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
                login_user(user)
                admin = user.admin
                if admin:
                    redirect(url_for('admin.adminroute'))
                else:
                    pass

    return render_template('login.html',form=form,msg=msg, error=error)

@auth.route('/signup', methods=['GET','POST'])
def signup():
    error = None
    msg = None
    form = RegisterForm()
    if form.validate_on_submit():
        pass1 = form.password1.data
        pass2 = form.password2.data
        if pass1 == pass2:
            regex = r"^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$"
            mail = form.email.data
            if re.match(regex,mail):
                ui = UserInformation()
                salt = get_random_string(10)
                password = hashing.hash_value(pass1,salt=salt)
                created_user = ui.create_user(mail,form.username.data,password,salt)
                if created_user is None:
                    return redirect(url_for('auth.login',msg='Du wurderst registriert! Du kannst dich jetzt anmelden.'))
                else:
                    return redirect(url_for('auth.signup',error=created_user))
            else:
                error = 'Deine E-Mail scheint falsch zu sein. Gib sie bitte erneut ein.'
        else:
            error = 'Deine Passwörter stimmen nicht überein. Gib sie bitte erneut ein.'
    return render_template('register.html',form=form,error=error)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


if __name__ == '__main__':
    app.run()
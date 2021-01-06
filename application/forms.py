
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Einloggen')

class RegisterForm(FlaskForm):
    email = StringField('E-Mail Adresse',validators=[DataRequired()])
    username = StringField('Benutzername',validators=[DataRequired()])
    password1 = PasswordField('Passwort', validators=[DataRequired()])
    password2 = PasswordField('Passwort bestätigen', validators=[DataRequired()])
    submit = SubmitField('Registrieren')

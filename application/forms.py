
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Einloggen')

class RegisterForm(FlaskForm):
    email = StringField('E-Mail Adresse',validators=[DataRequired(), Email(message="Gib eine gültige E-Mail-Adresse ein.")])
    username = StringField('Benutzername',validators=[DataRequired()])
    password1 = PasswordField('Passwort', validators=[DataRequired(), Length(min=6,message="Passwort muss länger als 6 Zeichen sein.")])
    password2 = PasswordField('Passwort bestätigen', validators=[DataRequired(), EqualTo('password1', message="Passwort muss mit vorherigem übereinstimmen.")])
    submit = SubmitField('Registrieren')

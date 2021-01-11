from flask_hashing import Hashing
from .models import db, User
import os

class UserInformation():
    def __init__(self):
        self.password = None
        self.username = None
        self.funktion = None
        self.admin = None
        self.mail = None
        self.userid = None
        self.salt = None
        self.activated = None
        self.hashing = Hashing()


    def check_existing_user(self,username,email):
        existing_user = User.query.filter(
            User.username == username or User.email == email
        ).first()
        return existing_user
        
    def create_user(self,email,username,password,funktion,salt):
        exists = self.check_existing_user(username,email)

        if exists:
            error = 'Benutzer ist bereits registriert.'
            return error
        else:
            if funktion == 'admin':
                self.admin = True
            else:
                self.admin = False
            self.funktion = funktion
            self.password = password
            self.mail = email
            self.username = username
            self.salt = salt
            self.activated = True
            new_user = User(
                username=self.username,
                email=self.mail,
                password=self.password,
                salt=self.salt,
                admin=self.admin,
                active=self.activated
            )
            db.session.add(new_user)
            db.session.commit()
            self.userid = new_user.id
            return None

    def get_funktion(self,*kwargs):
        THIS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(THIS_DIRECTORY,'whitelist.txt')
        file = open(filepath,'r')
        emailaddresses = file.readlines()
        funktion = None
        for address in emailaddresses:
            for kwarg in kwargs:
                if address == kwarg.lower():
                    funktion = 'admin'
                else:
                    funktion = 'nonadmin'
        self.funktion = funktion
        return funktion

    def get_user(self,username,password):
        user = User.query.filter(
            User.username == username
        ).first()

        if user:
            self.salt = user.salt
            self.password = user.password
            if self.verify_password(password):
                db.session.add(user)
                db.session.commit()
                return user, None
            else:
                error = 'Das eingegebene Passwort scheint falsch zu sein \n Versuche es erneut oder setze dein Passwort zurück.'
                return None, error
        else:
            error = 'Benutzer konnte nicht gefunden werden. \n Versuche es mit einem anderen Benutzernamen oder registriere dich.'
            return None, error

    def verify_password(self,password):
        return self.hashing.check_value(self.password,password,self.salt)
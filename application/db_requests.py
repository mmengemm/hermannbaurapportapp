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
        pass
    
    def get_user(self,username,password):
        user = User.query.filter(
            User.username == username
        ).first()

        if user:
            self.salt = user.salt
            self.password = user.password
            if self.verify_password(password):
                return user, None
            else:
                error = 'Das eingegebene Passwort scheint falsch zu sein \n Versuche es erneut oder setze dein Passwort zurück.'
                return None, error
        else:
            error = 'Benutzer konnte nicht gefunden werden. \n Versuche es mit einem anderen Benutzernamen oder registriere dich.'
            return None, error
            
    def verify_password(self,password):
        return self.hashing.check_value(self.password,password,self.salt)
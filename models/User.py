from database import db 
from werkzeug.security import check_password_hash, generate_password_hash
#import hashlib
from datetime import datetime as dt

class User (db.Model):
    __tablename="users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,unique=True, nullable=False)
    hash = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime())
    active = db.Column(db.Boolean(), nullable=False)



    def __init__(self, username, password, active=True ,created_at=dt.now()):
        self.username     = username
        #comrpueba las distintas reglas para aceptar un password válido
        if not User.check_password(password):
            raise Exception("Error : invalid password")
        self.hash        = User.generate_hash (password)      
        self.active      = active
        self.created_at  = created_at

    def __repr__(self):
        return '<User {}>'.format(self.username)

    #permite cambiar de password
    def changePassword(self,oldPassword, newPassword):
        if not User.check_password(newPassword):
            raise Exception("Error : invalid password")

        if (User.check_password_hash(self.hash,oldPassword)):
            self.hash = User.generate_hash(newPassword)
        else:    
            raise Exception("Error : invalid password")


#--------------------------------------------------------------

    @staticmethod
    def authenticate(username, password):
        lista = User.query.filter_by(username=username).all()
        if len(lista)!=1:
            raise Exception("Error : invalid username and/or password")
        user = lista[0]
        if (check_password_hash(user.hash,password)):
            return user
        else:
            raise Exception ("Error : invalid username and/or password")

     
    


  # check that is a valid password
    @staticmethod
    def check_password(password):
        if len(password)<4:
            return False
        digit = False
        alpha = False
        upper = False
        lower = False

        # check all characters that needs contains a password
        for character in password:
            digit = digit or character.isdigit()
            alpha = alpha or character.isalpha()
            upper = upper or character.isupper()
            lower = lower or character.islower()


        return (digit and alpha and upper and lower)

#genera el código hash del password facilitado
    @staticmethod
    def generate_hash (password):        
        return generate_password_hash(password)
#        return hashlib.sha224(password.encode("UTF-8")).hexdigest()
 #       return hashlib.sha224(password.encode("UTF-8")).hexdigest()
        #return (password)

    @staticmethod
    def check_password_hash (hash,oldpassword):
#      return (hash==hashlib.sha224(oldpassword.encode("UTF-8")).hexdigest())
 #     return (hash==oldpassword)
      return check_password_hash(hash,oldpassword)
        
        



#--------------------------------------------------------------




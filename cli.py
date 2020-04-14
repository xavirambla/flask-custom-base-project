import os 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from database import db
from models.User import User
from models.Book import Book




app = Flask(__name__)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")
#else:
 # print ("os.getenv(DATABASE_URL) : {}" .format(os.getenv("DATABASE_URL")))  

  # Set up database

app.config["SQLALCHEMY_DATABASE_URI"]  = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]  = True 

db.init_app(app)
app.app_context().push()

def reset_db_command():
    """Clear existing data and create new tables."""    
    db.drop_all()

def main ():
    print("CREATE_ALL")
    #reset_db_command()
    db.create_all()
    db.session.commit()
    print("END CREATE_ALL")


if __name__=="__main__":
    with app.app_context():
        main()


user = User.query.filter_by(username="user199").first()
if(not user is None):
    db.session.delete(user)
    db.session.commit()

user  = User (username ="user199" , password="aaaA1_.")

print ("User: {}".format(user))
db.session.add(user)
print(f"user.hash : {user.hash}")
db.session.commit()
user.changePassword("aaaA1_.","bbbB5_.")
db.session.commit()

user2 = User.query.get(user.id)
print(f"user2.hash : {user2.hash}")





"""

try:
    user = User.authenticate(username ="user1" , password="aaaA1_.")
    print ("OK - {}".format(user))
except Exception as error:
    print("KO . Usuario no encontrado")

try:
    User.authenticate(username ="user1" , password="a999_.")
except Exception as error:
    print ("OK si excepción : "+repr(error    ))

try:
    User.authenticate(username ="nobody" , password="aa1a_.")
except Exception as error:
    print ("OK si excepción : "+repr(error    ))


user  = User (username ="user2" , password="aaaA2_.", active=True)
db.session.add(user)

user  = User (username ="user3" , password="aaaA3_.", active=True)
db.session.add(user)
db.session.commit()

 

try:
    user_login = User.authenticate(username ="user1" , password="aaaA1_.")
    print ("OK : {}".format(user_login))
except Exception as error:
    print ("KO : "+repr(error    ))

try:
    user_login.changePassword("adfasdfsd","fdsa")
    print("KO - changePassword")
except Exception as error:
    print ("OK : "+repr(error    ))
try:
    user_login.changePassword("aa1a_.","fdsa")
    print("KO - changePassword")
except Exception as error:
    print ("OK : "+repr(error    ))

try:
    user_login.changePassword("aaaA1_.","Aa9a_.")
    print("OK - changePassword")    

except Exception as error:
    print ("KO : "+repr(error    ))
db.session.commit()

try:
    user_login = User.authenticate(username ="user1" , password="aaaA1_.")
    print("KO - Authenticate")
except Exception as error:
    print ("OK : "+repr(error    ))


try:
    user_login = User.authenticate(username ="user1" , password="Aa9a_.")
    print("OK - Authenticate")    
except Exception as error:
    print ("KO : "+repr(error    ))



lista = User.query.all()
print ("queryAll: {}".format(lista))
"""



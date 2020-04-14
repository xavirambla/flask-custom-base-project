import os 
import csv 
from database import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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


def loadCSV(filename):
    with open(filename,"r") as fileCSV:
        reader = csv.DictReader(fileCSV)
        for row in reader:
#            print(f"{row}")
#            print (f"{row['isbn']}")
            book = Book ( isbn =row['isbn'] ,  title =row['title'] ,  author =row['author'] ,  year =row['year']  )
            db.session.add(book)
    db.session.commit()
    lista = Book.query.all()
    print ("queryAll: {}".format(lista))

def main ():
    print("CREATE_ALL")
    loadCSV("books.csv")
    db.session.close() 
    





if __name__=="__main__":
    with app.app_context():
        main()


"""


user  = User (username ="user1" , password="aaaA1_.")
print ("User: {}".format(user))
db.session.add(user)

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
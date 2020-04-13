import os

from flask import Flask, session, render_template,  request,redirect,url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from models.User import User


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


  # Set up database
app.config["SQLALCHEMY_DATABASE_URI"]  = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]  = False 

db = SQLAlchemy()
db.init_app(app)

#--------------------------------------------------------------------------
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:    
            if session["user_id"] is None:
                return redirect(url_for('login', next=request.url))
        except KeyError:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

#--------------------------------------------------------------------------


@app.route("/")
def index():
    return render_template("index.html")
#    return "Project 1: TODO"

#------------------------------------------------------------------------------------
@app.route("/register", methods=["POST","GET"])
def register():
    if request.method=="POST":
        #dar de alta
        username  = request.form.get("username")
        password = request.form.get("password")

        if not username or not password :
            return render_template("register.html",error = "User/Password is Empty" )
        try:            
            user =User.query.filter_by(username=username).first()
            if user is None:
                user  = User (username =username , password=password, active=True)
                db.session.add(user)
                db.session.commit()
            # Remember which user has logged in
                user_id = user.id 
                session["user_id"] = user_id
                return render_template("index.html",message = "Created user", user =user ) 

            else:
                return render_template("register.html",error = "user exists. Try with another username" )   

        except Exception as error:   
            return render_template("register.html",error = str(error) )
            
    else:
        return render_template("register.html")

#------------------------------------------------------------------------------------
@app.route("/login", methods=["POST","GET"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method=="POST":

        #dar de alta
        usuario  = request.form.get("username")
        password = request.form.get("password")


        if not usuario or not password :
            return render_template("login.html",error = "User/Password is Empty" )
        try:
            user = User.authenticate(username = usuario,password = password)
  
            # Remember which user has logged in
            user_id = user.id 
            session["user_id"] = user_id
            return render_template("index.html",message = "Login it", user =user ) 

        except Exception as error:   
            return render_template("login.html",error = str(error) )
    else:
        return render_template("login.html")


#------------------------------------------------------------------------------------
@app.route("/changePassword", methods=["POST","GET"])
@login_required
def changePassword():

    if request.method=="POST":
        #get values of password.
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        user_id = session["user_id"] 
        user = User.query.get(user_id)
        if user is None:
            print  (f"Error to recovery user_id {user_id}")
            return  render_template("changepassword.html",error="Error to recovery user_id")
        else:
            try:
                user.changePassword(old_password,new_password)
                db.session.commit()
                return render_template("index.html",message = "Password change it", user =user ) 
            except Exception as error:   
                return render_template("changepassword.html",error = str(error) )      
    else:
        return render_template("changepassword.html")



@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return render_template("index.html",message = "Bye Bye")
    


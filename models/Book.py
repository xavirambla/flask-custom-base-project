from database import db 
#import hashlib

class Book (db.Model):
    __tablename="books"


    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, unique=True,nullable=False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)



    def __init__(self, isbn, title, author, year ):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year 

    def __repr__(self):
        return '<Book {} - {} >'.format(self.isbn,self.title )


        
        



#--------------------------------------------------------------




import unittest

from models.Book import Book
from models.User import User
from database import db
from application import app
from selenium import webdriver
from flask import url_for




__test__={            
            "run_all" : True,  # run all tests             
              "run_class": True,  # run class test
                "run_httpModel" : False,   # run httpModel test 
                "run_httpMethods" : True,  # run httpMethods test        
            }

#app.app_context().push() 



#-----------------


#-----------------





@unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_class"] )  ,
                     "not required check Models in this test")
class Book_TestCase (unittest.TestCase):
    def setUp(self):
             
        with app.app_context():
            
            db.session.close() 



            """
            db.drop_all()            
            db.create_all()

            """
        # creates a test client
            self.app = app.test_client()
        # propagate the exceptions to the test client
            self.app.testing = True 



        db.session.commit()        
        book = Book ( isbn ="isbn_test1" ,  title ="test1" ,  author ="test1" ,  year =2000 )
        db.session.add(book)
        book = Book ( isbn ="isbn_test2" ,  title ="test2" ,  author ="test1" ,  year =2001 )
        db.session.add(book)
        book = Book ( isbn ="isbn_test3" ,  title ="test2" ,  author ="test2" ,  year =2002 )
        db.session.add(book)        
        book = Book ( isbn ="isbn_test4" ,  title ="test3" ,  author ="test2" ,  year =2003 )
        db.session.add(book)        
        book = Book ( isbn ="isbn_test5" ,  title ="test3" ,  author ="test2" ,  year =2000 )
        db.session.add(book)

        user = User(username ="book_test" , password="aaaA1_.")
        db.session.add(user)        

        db.session.commit()
        client = self.app
        login(client, username = "book_test", password="aaaA1_.")

            
    def tearDown(self):
        client = self.app
        logout(client)

        oldBook = Book.query.filter_by(isbn="isbn_test1").first()
        if ( oldBook):
            db.session.delete(oldBook)
        oldBook = Book.query.filter_by(isbn="isbn_test2").first()
        if ( oldBook):
            db.session.delete(oldBook)
        oldBook = Book.query.filter_by(isbn="isbn_test3").first()
        if ( oldBook):
            db.session.delete(oldBook)
        oldBook = Book.query.filter_by(isbn="isbn_test4").first()
        if ( oldBook):
            db.session.delete(oldBook)
        oldBook = Book.query.filter_by(isbn="isbn_test5").first()
        if ( oldBook):
            db.session.delete(oldBook)

        oldBook = Book.query.filter_by(isbn="isbn_test5").first()
        if ( oldBook):
            db.session.delete(oldBook)

        oldUser = User.query.filter_by(username ="book_test").first()        
        db.session.delete(oldUser)        

        db.session.commit()



        db.session.close()            
        db.session.remove()  
            



    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_findBookByISBN(self):
        lista = Book.query.filter_by(isbn="isbn_test1")
        num = lista.count()
        self.assertEqual(1,num)
        book  = lista.first()
        self.assertEqual(book.isbn,"isbn_test1")
        pass
        

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_findBookByTitle(self):
        lista = Book.query.filter_by(title="test1")
        num = lista.count()
        self.assertEqual(1,num)
        book  = lista.first()
        self.assertEqual(book.isbn,"isbn_test1")
        pass

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_findBookByAuthor(self):
        lista = Book.query.filter_by(author="test1")
        num = lista.count()
        self.assertEqual(2,num)
        book  = lista.first()
        self.assertEqual(book.isbn,"isbn_test1")
        pass

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_findBookByYear(self):
        lista = Book.query.filter_by(year=2000)
        num = lista.count()
        self.assertEqual(2,num)
        book  = lista.first()
        self.assertEqual(book.isbn,"isbn_test1")
        pass




#--------------------------------------------------------------------------
#---------- Web testing templates  ------------------------------------------------
#--------------------------------------------------------------------------


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_search_status_code(self):
        client = self.app 
        response = client.get('/search') 

        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_search_data(self):
        client = self.app 
        response = client.get('/search') 

        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 
        assert b'SEARCH' in response.data
        assert b'ISBN' in response.data


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_search_byTitle(self):
        # sends HTTP GET request to the application
        client = self.app 
        response = client.post('/search', data=dict(
                                isbn="",
                                title="test1",
                                author="",
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        assert b'List of Books' in response.data
        assert b'test1' in response.data


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_search_NoData(self):
        # sends HTTP GET request to the application
        client = self.app 
        response = client.post('/search', data=dict(
                                isbn="",
                                title="Nodata",
                                author="",
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        assert b'No books in database' in response.data



    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_search_byISBN(self):
        # sends HTTP GET request to the application
        client = self.app 
        response = client.post('/search', data=dict(
                                isbn="isbn_test2",
                                title="",
                                author="",
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        assert b'List of Books' in response.data
        assert b'test2' in response.data



    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_search_byAuthor(self):
        # sends HTTP GET request to the application
        client = self.app 
        response = client.post('/search', data=dict(
                                isbn="",
                                title="",
                                author="test2",
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        assert b'List of Books' in response.data
        assert b'isbn_test3' in response.data
        assert b'isbn_test4' in response.data
        assert b'isbn_test5' in response.data




    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_search_byTitleAndAuthor(self):
        # sends HTTP GET request to the application
        client = self.app 
        response = client.post('/search', data=dict(
                                isbn="",
                                title="test2",
                                author="test1",
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        assert b'List of Books' in response.data
        assert b'isbn_test2' in response.data




    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_search_byAuthorLike(self):
        # sends HTTP GET request to the application
        client = self.app 
        response = client.post('/search', data=dict(
                                isbn="",
                                title="",
                                author="t1",
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        assert b'List of Books' in response.data
        assert b'isbn_test1' in response.data
        assert b'isbn_test2' in response.data

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_search_byTitleLike(self):
        # sends HTTP GET request to the application
        client = self.app 
        response = client.post('/search', data=dict(
                                isbn="",
                                title="t",
                                author="",
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        assert b'List of Books' in response.data
        assert b'isbn_test1' in response.data
        assert b'isbn_test2' in response.data
        assert b'isbn_test3' in response.data        
        assert b'isbn_test4' in response.data        
        assert b'isbn_test5' in response.data


#-------------------------------------------------------------------------------------------------

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)


if __name__=="__main__":
    unittest.main()

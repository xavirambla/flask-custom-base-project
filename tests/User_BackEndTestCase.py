import unittest

from models.User import User

from database import db
from application import app
from selenium import webdriver
from flask import url_for


__test__={            
            "run_all" : True,  # run all tests             
              "run_class": False,  # run class test
                "run_httpModel" : False,   # run httpModel test 
                "run_httpMethods" : False,  # run httpMethods test        
            }

#app.app_context().push() 



#-----------------


#-----------------





@unittest.skipIf( not  (__test__["run_all"]  or  __test__["run_class"] )  ,
                     "not required check Models in this test")
class User_TestCase (unittest.TestCase):
    def setUp(self):
             
        with app.app_context():
            
            db.session.close() 
            db.drop_all()            
            db.create_all()

        # creates a test client
            self.app = app.test_client()
        # propagate the exceptions to the test client
            self.app.testing = True 




        a1 = User(username ="test1" , password="aaaA1_.")
        db.session.add(a1)
        a2 = User(username ="test2" , password="aaaA1_.")
        db.session.add(a2)
        a3 = User(username ="test3" , password="aaaA1_.")
        db.session.add(a3)
        a4 = User(username ="test4" , password="aaaA1_.")
        db.session.add(a4)
        a5 = User(username ="test5" , password="aaaA1_.")
        db.session.add(a5)
        db.session.commit()
            
    def tearDown(self):
        db.session.close()            
        db.session.remove()  
            
    """
    def tearDown(self):
        print ("tearDown start")        
        with app.app_context():
            # Elimina todas las tablas de la base de datos
            db.session.expunge_all()
            db.session.close()            
            db.session.remove()
            print ("db.drop_all() start")            
            db.drop_all()
            print ("drop all")            
            print ("db.session.remove()")

        app.app_context().pop()
        print ("tearDown end")        
    
    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["skip_httpModel"] )  ,
                     "not required check Models in this test")
    def test2(self):        
        self.assertTrue(True)
    """

#------------ new user -------------------------------------------
    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_newUser(self):
        try:
            user  = User (username ="user1" , password="aaaA1_.")
            db.session.add(user)
            db.session.commit()
            self.assertTrue(not user is None)
        except Exception as error:
             self.fail(str(error))


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_newUser1(self):
        try:
            user  = User (username ="user1" , password="aaaA1_.", active=True)
            db.session.add(user)
            db.session.commit()
            self.assertTrue(not user is None)
        except Exception as error:
             self.fail(str(error))



    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_newUser_badPass(self):
        try:
            user  = User (username ="user1" , password="aaa_.")
            db.session.add(user)
            db.session.commit()
            self.fail("Error - No debería permitir crear un usuario con un password que no cumple los requisitos mínimos")
        except Exception as error:
            pass

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_newUser_noPass(self):
        try:
            user  = User (username ="user1" , password="")
            db.session.add(user)
            db.session.commit()
            self.fail("Error - No debería permitir crear un usuario sin password")
        except Exception as error:
            pass

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_newUser_noUser(self):
        try:
            user  = User (username ="" , password="aaaA1_.")
            db.session.add(user)
            db.session.commit()
            self.fail("Error - No debería permitir crear un usuario sin nombre")
        except Exception as error:
            pass

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_newUser_existing(self):
        try:
            user  = User (username ="user2" , password="aaaA1_.")
            user2  = User (username ="user2" , password="aaaA1_.")
            db.session.add(user)
            db.session.add(use2)

            db.session.commit();
            self.fail("Error - No debería permitir crear un usuario que ya existe")
        except Exception as error:
            pass

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_newUser_existing2(self):
        try:
            user  = User (username ="user2" , password="aaaA1_.")
            db.session.add(user)
            db.session.commit()
            user2  = User (username ="user2" , password="aaaA1_.")
            db.session.add(use2)
            db.session.commit()
            self.fail("Error - No debería permitir crear un usuario que ya existe")
            
        except Exception as error:
            pass           
#---------- list  --------------------------------------------------
    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_listUsers(self):
        lista = User.query.all()
        self.assertTrue(len(lista)==5)

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_findUserByUsername(self):
        num = User.query.filter_by(username="test2").count()       
        self.assertTrue(num==1)


#---------- login --------------------------------------------------
    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_authenticate(self):
        try:
            user = User.authenticate(username ="test5" , password="aaaA1_.")
            self.assertTrue(not user is None)
        except Exception as error:
             self.fail(str(error))


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_authenticate_noUser(self):
        try:
            user = User.authenticate(username ="test555" , password="aaaA1_.")
            self.assertTrue(False)
        except Exception as error:
            pass


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_authenticate_noPassword(self):
        try:
            user = User.authenticate(username ="test5" , password="___A1_.")
            self.assertTrue(False)
        except Exception as error:
            pass
#---------- change password --------------------------------------------------
    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_changePassword(self):
        try:
            user = User.authenticate(username ="test5" , password="aaaA1_.")
            old_hash= user.hash
            user.changePassword("aaaA1_.","bbbB2_.")
            db.session.merge(user)
            db.session.commit();
            user2 = User.query.get(user.id)
            self.assertFalse(old_hash ==user2.hash)            
        except Exception as error:
             self.fail(str(error))

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_changePassword_badOldPassword(self):
        try:
            user = User.authenticate(username ="test5" , password="aaaA1_.")
            user.changePassword("cccA1_.","bbbB2_.")
            db.session.merge(user)
            db.session.commit();
            self.fail("Error - Password antigo es incorrecto y debería haber fallado")
        except Exception as error:
            pass


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_changePassword_badNewPassword(self):
        try:
            user = User.authenticate(username ="test5" , password="aaaA1_.")
            user.changePassword("aaaA1_.","111111")
            db.session.merge(user)
            db.session.commit();
            self.fail("Error - Password nuevo es incorrecto y debería haber fallado")
        except Exception as error:
             pass

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_changePassword_andAuthenticate(self):
        try:
            user = User.authenticate(username ="test5" , password="aaaA1_.")
            user.changePassword("aaaA1_.","bbbB2_.")
            db.session.merge(user)
            db.session.commit();

            user2 = User.authenticate(username ="test5" , password="bbbB2_.")
            self.assertTrue(not user is None)

            pass
        except Exception as error:
             self.fail(str(error))

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_changePassword_andAuthenticateUsingOldPassword(self):
        try:
            user = User.authenticate(username ="test5" , password="aaaA1_.")
            user.changePassword("aaaA1_.","bbbB2_.")
            db.session.merge(user)
            db.session.commit();

            user2 = User.authenticate(username ="test5" , password="aaaA1_.")
            self.fail("Error - Password viejo usado y no debería haber autentificado")            
        except Exception as error:
            pass
             

#---------- check_password --------------------------------------------------
    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_checkPassword(self):
        self.assertTrue(User.check_password("aA1.aa"))

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_checkPassword_badPasswordLength(self):
        self.assertFalse(User.check_password("a"))

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_checkPassword_badPasswordNumber(self):
        self.assertFalse(User.check_password("aAaAA."))

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_checkPassword_badPasswordUpper(self):
        self.assertFalse(User.check_password("aaaa1."))

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_checkPassword_badPasswordLower(self):
        self.assertFalse(User.check_password("AAAA1."))


#---------- generateHash --------------------------------------------------
    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpModel"] )  ,
                     "not required check Models in this test")
    def test_generateHash(self):
        hash = User.generate_hash ("password")
        self.assertTrue(len(hash)>20)


#--------------------------------------------------------------------------
#---------- Web testing templates  ------------------------------------------------
#--------------------------------------------------------------------------


#----------------------------------------------------------
    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        client = self.app 
        response = client.get('/') 

        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_home_data(self):
        # sends HTTP GET request to the application
        client = self.app 

        # on the specified path
        response = client.get('/') 
        self.assertEqual(response.status_code, 200) 
        assert b'Hello World!!!' in response.data



#---------- login  ------------------------------------------------
    
    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_login_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        client = self.app 
        response = client.get('/login') 

        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 
        

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_login_data(self):
        # sends HTTP GET request to the application
        client = self.app 

        # on the specified path
        response = client.get('/login') 
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data

        assert b'LOGIN' in response.data
        assert b'username' in response.data
        assert b'password' in response.data
        assert b'Log In' in response.data
        assert b'action="/login"' in response.data   


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_login_authenticate(self):
        # sends HTTP GET request to the application
        client = self.app 
        response = client.post('/login', data=dict(
                                username="test2",
                                password="aaaA1_."
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data

        assert b'test2' in response.data
        assert b'/logout' in response.data

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_login_authenticate_userIncorrect(self):
        # sends HTTP GET request to the application
        client = self.app 
        response = client.post('/login', data=dict(
                                username="test_",
                                password="aaaA1_."
                                ), follow_redirects=True)

        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        assert b'LOGIN' in response.data
        assert b'username' in response.data
        assert b'password' in response.data
        assert b'Log In' in response.data
        assert b'action="/login"' in response.data   

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_login_authenticate_userIncorrect2(self):
        # sends HTTP GET request to the application
        client = self.app 
        response = client.post('/login', data=dict(
                                username="test2",
                                password="a_."
                                ), follow_redirects=True)

        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        assert b'LOGIN' in response.data
        assert b'username' in response.data
        assert b'password' in response.data
        assert b'Log In' in response.data
        assert b'action="/login"' in response.data   


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_login_logout(self):
        # sends HTTP GET request to the application
        client = self.app 
        response = client.post('/login', data=dict(
                                username="test2",
                                password="aaaA1_."
                                ), follow_redirects=True)

        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data

        assert b'test2' in response.data
        assert b'/logout' in response.data

        response = client.get('/logout', follow_redirects=True)
        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        assert b'/login' in response.data



 #---------- register ------------------------------------------------
    
    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_register_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        client = self.app 
        response = client.get('/register') 

        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 
        

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_register_data(self):
        # sends HTTP GET request to the application
        client = self.app 

        # on the specified path
        response = client.get('/register') 
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        self.assertIn(b'REGISTER', response.data)



        assert b'REGISTER' in response.data
        assert b'username' in response.data
        assert b'password' in response.data
        assert b'Save' in response.data
        assert b'action="/register"' in response.data      




    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_register_createUser_(self):
        # sends HTTP GET request to the application
        client = self.app 
        username  = "aaaB1"        
        password  = "_.aA1aA"
#        self.assertTrue(True)
        
        response =  client.post('/register', data=dict(
                                username=username,
                                password=password
                                ), follow_redirects=True)
        self.assertEqual(response.status_code, 200) 
     

        # on the specified path
        self.assertEqual(response.status_code, 200) 


        data = response.data.decode("UTF-8")        
        result  = ( username in data)
        self.assertTrue( result)
        self.assertIn( b'logout', response.data)
        self.assertIn( b'Created user', response.data)
        assert b'Created user' in response.data




    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_register_DuplicatedUser(self):

        # sends HTTP GET request to the application 
        client = self.app 
        username  = "aaaB1"        
        password  = "a1A333S_."
        #USuario correcto
        response =  client.post('/register', data=dict(
                                username=username,
                                password=password
                                ), follow_redirects=True)        
        #Creamos el mismo usuario                        
        response =  client.post('/register', data=dict(
                                username=username,
                                password=password
                                ), follow_redirects=True)        

        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
        self.assertIn (b'/register', response.data)
        self.assertIn (b'username', response.data)
        self.assertIn (b'password', response.data)
        self.assertIn (b'alert alert-danger', response.data)


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_register_badPassword(self):
        # sends HTTP GET request to the application 
        client = self.app 
        username  = "aaa2B"        
        password  = "a1."
        #USuario correcto
        response =  client.post('/register', data=dict(
                                username=username,
                                password=password
                                ), follow_redirects=True)        

        # on the specified path
        self.assertEqual(response.status_code, 200) 
        
        # assert the response data
#        print (f"kouser: {response.data}")
        self.assertIn (b'/register', response.data)
        self.assertIn (b'username', response.data)
        self.assertIn (b'password', response.data)
        self.assertIn (b'alert alert-danger', response.data)

#---------------------------------- Change PAssword  ---------------------------
  
    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_changePassword_status_code(self):
        # sends HTTP GET request to the application
        client = self.app 
        username  = "test2"
        password  = "aaaA1_."
        response = client.post('/login', data=dict(
                                username = username,
                                password = password
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200)         

        
        # on the specified path        
        response = client.get('/changePassword') 

        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 
        



    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_changePassword_data(self):
        # sends HTTP GET request to the application
        client = self.app 
        username  = "test2"
        password  = "aaaA1_."
        response = client.post('/login', data=dict(
                                username = username,
                                password = password
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200)         

        
        # on the specified path        
        response = client.get('/changePassword') 

        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 
        # assert the response data
        self.assertIn(b'Change Password', response.data)





    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_changePassword_okOperation(self):
        # sends HTTP GET request to the application
        client = self.app 
        username  = "test2"
        password  = "aaaA1_."
        response = client.post('/login', data=dict(
                                username = username,
                                password = password
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200)         
        # on the specified path        
        response = client.post('/changePassword', data=dict(
                                old_password = password,
                                new_password = password+".."
                                ), follow_redirects=True)

        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 
        # assert the response data
        self.assertIn(b'Password change it', response.data)



    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_changePassword_badNewPassword(self):
        # sends HTTP GET request to the application
        client = self.app 
        username  = "test2"
        password  = "aaaA1_."
        response = client.post('/login', data=dict(
                                username = username,
                                password = password
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200)         
        # on the specified path        
        response = client.post('/changePassword', data=dict(
                                old_password = password,
                                new_password = ".."
                                ), follow_redirects=True)

        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 
        # assert the response data
        self.assertIn (b'alert alert-danger', response.data)


    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_changePassword_badOldPassword(self):
        # sends HTTP GET request to the application
        client = self.app 
        username  = "test2"
        password  = "aaaA1_."
        response = client.post('/login', data=dict(
                                username = username,
                                password = password
                                ), follow_redirects=True)


        # on the specified path
        self.assertEqual(response.status_code, 200)         
        # on the specified path        
        response = client.post('/changePassword', data=dict(
                                old_password = password+"0",
                                new_password = password+".e3"
                                ), follow_redirects=True)

        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 
        # assert the response data
        self.assertIn (b'alert alert-danger', response.data)




    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_httpMethods"] )  ,   
                     "not required http methods in this test")
    def test_changePassword_notAuthenticate(self):
        # sends HTTP GET request to the application
        client = self.app 
        username  = "test2"
        password  = "aaaA1_."
        # on the specified path        
        response = client.post('/changePassword', data=dict(
                                old_password = password,
                                new_password = password+".e3"
                                ), follow_redirects=True)

        # assert the status code of the response
        self.assertEqual(response.status_code, 200) 
        # assert the response data
        self.assertIn (b'/login', response.data)
        self.assertNotIn(b'/logout', response.data)        


#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

         


"""
        a4 = User(username ="test4" , password="aaaA1_.")
        
        def register(client, username, password):
    return client.post('/register', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)



def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)
"""

"""
 with self.assertRaises(TypeError):
     aaaa
pass
"""

"""
with self.assertRaises(SomeException) as cm:
    do_something()

the_exception = cm.exception
self.assertEqual(the_exception.error_code, 3)

"""

if __name__=="__main__":
    unittest.main()

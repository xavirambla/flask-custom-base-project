import unittest

from models.User import User
from database import db
from application import app
from selenium import webdriver
from flask import url_for
import time 


#__browser__="chrome"
__browser__="firefox"
# list of browsers : chrome, firefox


__test__={            
            "run_all" :False,  # run all tests             
              "run_class": True,  # run class test
                "run_JavascriptMethods" : False,   # run JavascriptMethods test                   
            }

#app.app_context().push() 

#__time_between_pages__ = 5 # define el tiempo entre solicitar una web y visitarla
__time_between_pages__ = 8 # define el tiempo entre solicitar una web y visitarla

#-----------------
def getDriverForBrowser(browser):
    switcher = {
        "chrome": webdriver.Chrome(),
        "firefox": webdriver.Firefox(),
    }
    return switcher[browser]


#-----------------





@unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_class"] )  ,
                     "not required check Models in this test")
class User_TestCase (unittest.TestCase):
    def setUp(self):
#        print ("setUp Start")
        with app.app_context():
#            try:
#                if not self.driver is None:
#                    print ("self.driver.close()1")
#                    self.driver.close()        
#                    print ("self.driver.close()2")                    
#            except AttributeError:
#                nada=0        
            db.session.close() 
            #db.drop_all()       
           # db.create_all()

        # creates a test client
            self.app = app.test_client()
        # propagate the exceptions to the test client
            self.app.testing = False
            self.driver = getDriverForBrowser(__browser__)

            self.server_url  = "http://127.0.0.1:5000"
 #       print ("setUp End")

            
    def tearDown(self):
  #      print ("tearDown Start")
        self.driver.quit()
        #self.driver.close()         
        db.session.close()    
   #     print ("tearDown End")

#        db.session.remove()  
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

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

# ------------ Login ------------------

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_JavascriptMethods"] )  ,   
                     "not required http methods in this test")
    def test_loginButton(self):
        user  = "test3"
        passw =  "aaaA1_."
        
        url = self.server_url
        driver = self.driver
        
        driver.get(url)

        login_action(testCase = self, user = user, passw = passw )

        mainContent = driver.find_element_by_id("MainContent")
        self.assertEqual(  mainContent.text , f"Hello {user}!!!"  )



    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_JavascriptMethods"] )  ,   
                     "not required http methods in this test")
    def test_loginButton_KO(self):
        user  = "test3"
        passw =  "aaaA1_."

        url = self.server_url
        driver = self.driver
        
        driver.get(url)

        login_action(testCase = self, user = user, passw = passw+"erroneo" )

        titulo = driver.find_element_by_xpath(("//h1[@class='alert alert-primary']"))
        error = driver.find_element_by_xpath("//h5[@class='alert alert-danger']")
        self.assertIsNotNone(titulo)
        self.assertIsNotNone(error)
        

    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_JavascriptMethods"] )  ,   
                     "not required http methods in this test")
    def test_registerButton(self):
        user  = "test99"
        passw =  "aaaA1_."

        oldUser = User.query.filter_by(username=user).first()
        if ( oldUser):
            db.session.delete(oldUser)
            db.session.commit()

        url = self.server_url
        driver = self.driver
        
        driver.get(url)

        register_action(self, user, passw )

        mainContent = driver.find_element_by_id("MainContent")
        self.assertEqual(  mainContent.text , f"Hello {user}!!!"  )

        oldUser = User.query.filter_by(username=user).first()
        if ( oldUser):
            db.session.delete(oldUser)
            db.session.commit()




    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_JavascriptMethods"] )  ,   
                     "not required http methods in this test")
    def test_registerAndLogoutButton(self):
        user  = "test99"
        passw =  "aaaA1_."

        oldUser = User.query.filter_by(username=user).first()
        if ( oldUser):
            db.session.delete(oldUser)
            db.session.commit()

        url = self.server_url
        driver = self.driver
        
        driver.get(url)

        register_action(self, user, passw )
        mainContent = driver.find_element_by_id("MainContent")
        self.assertEqual(  mainContent.text , f"Hello {user}!!!"  )

        logout_action(self)

        oldUser = User.query.filter_by(username=user).first()
        if ( oldUser):
            db.session.delete(oldUser)
            db.session.commit()



    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_JavascriptMethods"] )  ,   
                     "not required http methods in this test")
    def test_RegisterAndChangePasswordButton(self):
        user  = "test99"
        passw =  "aaaA1_."

        oldUser = User.query.filter_by(username=user).first()
        if ( oldUser):
            db.session.delete(oldUser)
            db.session.commit()

        url = self.server_url
        driver = self.driver
        
        driver.get(url)

        register_action(self, user, passw )
 #       html_source = driver.page_source
 #       print (f"Page : {html_source}")

        mainContent = driver.find_element_by_id("MainContent")
        self.assertEqual(  mainContent.text , f"Hello {user}!!!"  )

        changePassword_action(self,old_password = passw, new_password= passw+"new")

        titulo = driver.find_element_by_xpath(("//h2[@class='alert alert-primary']"))
        self.assertIsNotNone(titulo)

        oldUser = User.query.filter_by(username=user).first()
        if ( oldUser):
            db.session.delete(oldUser)
            db.session.commit()




    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_JavascriptMethods"] )  ,   
                     "not required http methods in this test")
    def test_RegisterChangePasswordAndLoginOldPasswordButton(self):
        print("-- test_RegisterChangePasswordAndLoginOldPasswordButton --")
        user  = "test99"
        passw =  "aaaA1_."

        oldUser = User.query.filter_by(username=user).first()
        if ( oldUser):
            db.session.delete(oldUser)
            db.session.commit()

        url = self.server_url
        driver = self.driver
        
        driver.get(url)

        register_action(self, user, passw )
        # Inside
        mainContent = driver.find_element_by_id("MainContent")
        self.assertEqual(  mainContent.text , f"Hello {user}!!!"  )

        # change password page
        changePassword_action(self,old_password = passw, new_password= passw+"new")

        titulo = driver.find_element_by_xpath(("//h2[@class='alert alert-primary']"))
        self.assertIsNotNone(titulo)

        #logout 
        logout_action(self)
        login_action(self,user, passw )
        
        error = driver.find_element_by_xpath("//h5[@class='alert alert-danger']")
        titulo = driver.find_element_by_xpath(("//h1[@class='alert alert-primary']"))

        self.assertIsNotNone(titulo)
        self.assertIsNotNone(error)

        oldUser = User.query.filter_by(username=user).first()
        if ( oldUser):
            db.session.delete(oldUser)
            db.session.commit()



    @unittest.skipIf( not  (__test__["run_all"]  or   __test__["run_JavascriptMethods"] )  ,   
                     "not required http methods in this test")
    def test_RegisterChangePasswordAndLoginNewPasswordButton(self):
        print("-- test_RegisterChangePasswordAndLoginNewPasswordButton --")
        user  = "test99"
        passw =  "aaaA1_."

        oldUser = User.query.filter_by(username=user).first()
        if ( oldUser):
            db.session.delete(oldUser)
            db.session.commit()

        url = self.server_url
        driver = self.driver
        
        driver.get(url)

        register_action(self, user, passw )
        # Inside
        mainContent = driver.find_element_by_id("MainContent")
        self.assertEqual(  mainContent.text , f"Hello {user}!!!"  )

        # change password page
        changePassword_action(self,old_password = passw, new_password= passw+"new")

        titulo = driver.find_element_by_xpath(("//h2[@class='alert alert-primary']"))
        self.assertIsNotNone(titulo)


        #logout 
        logout_action(self)
        login_action(self,user, passw+"new" )
        # Inside
        html_source = driver.page_source
        
        mainContent = driver.find_element_by_id("MainContent")
        self.assertEqual(  mainContent.text , f"Hello {user}!!!"  )


        oldUser = User.query.filter_by(username=user).first()
        if ( oldUser):
            db.session.delete(oldUser)
            db.session.commit()








#-----------------------------------------------------------------------------
def login_action(testCase,user, passw ):    
    driver = testCase.driver
    login = driver.find_element_by_link_text('Log In')
    testCase.assertIsNotNone(login)
    login.click()
    time.sleep(__time_between_pages__)

    username = driver.find_element_by_xpath("//input[@name='username']")
    testCase.assertIsNotNone(username)
    password = driver.find_element_by_xpath("//input[@name='password']")
    testCase.assertIsNotNone(password)
    login_form = driver.find_element_by_id("login_form")
    testCase.assertIsNotNone(login_form )
    
    username.send_keys(user)
    password.send_keys(passw)
        
    login_form = driver.find_element_by_id("login_form")
    login_form.submit()    
    time.sleep(__time_between_pages__)

def register_action(testCase, user, passw ):    
    driver = testCase.driver    
    register = driver.find_element_by_link_text('Register')
    testCase.assertIsNotNone(register)
    register.click()
    time.sleep(__time_between_pages__)

    username = driver.find_element_by_xpath("//input[@name='username']")
    password = driver.find_element_by_xpath("//input[@name='password']")    
    register_form = driver.find_element_by_id("register_form")

    testCase.assertIsNotNone(username)
    testCase.assertIsNotNone(password)    
    testCase.assertIsNotNone(register_form )
        
    username.send_keys(user)
    password.send_keys(passw)            
    register_form.submit()
#    print (f"Register : {register_form}" )
    time.sleep(__time_between_pages__+10) #la opción register tada un poco más


def changePassword_action(testCase, old_password, new_password ):        
    driver = testCase.driver    
    changePassword = driver.find_element_by_link_text('Change Password')
    testCase.assertIsNotNone(changePassword)
    changePassword.click()
    time.sleep(__time_between_pages__)
    changepassword_form = driver.find_element_by_id("changepassword_form")
    testCase.assertIsNotNone(changepassword_form )
    txt_old_password = driver.find_element_by_xpath("//input[@name='old_password']")
    txt_new_password = driver.find_element_by_xpath("//input[@name='new_password']")
    testCase.assertIsNotNone(txt_old_password)
    testCase.assertIsNotNone(txt_new_password)

    txt_old_password.send_keys(old_password)
    txt_new_password.send_keys(new_password)

    changepassword_form.submit()
    time.sleep(__time_between_pages__)    


def logout_action(testCase):
    driver = testCase.driver 
    logout = driver.find_element_by_link_text('Log Out')
    testCase.assertIsNotNone(logout)
    logout.click()
    time.sleep(__time_between_pages__)
    titulo = driver.find_element_by_xpath(("//h2[@class='alert alert-primary']"))
    testCase.assertIsNotNone(titulo)




if __name__=="__main__":
    unittest.main()

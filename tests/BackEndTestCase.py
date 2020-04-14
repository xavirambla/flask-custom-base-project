import unittest
from application import app

from tests.User_BackEndTestCase import User_TestCase 
from tests.Book_BackEndTestCase import Book_TestCase 





class TestClass(unittest.TestCase):
    def setUp(self):
        print("setup_A")          
        with app.app_context():
            print("setup_A__")          
    def tearDown(self):
            print("tearDown_A")      


class TestClassA(unittest.TestCase):
    def setUp(self):
        print("setup_A")          
        with app.app_context():
            print("setup_A__")          
    def tearDown(self):
            print("tearDown_A")          

    def testOne(self):
        # test code
        print ("A")
        pass

class TestClassB(unittest.TestCase):
    def setUp(self):
        print("setup_B")          
        with app.app_context():
            print("setup_B__")          
    def tearDown(self):
            print("tearDown_B")          

    def testOne(self):
        # test code
        print ("B")

        pass

class TestClassC(unittest.TestCase):
    def setUp(self):
        print("setup_C")          
        with app.app_context():
            print("setup_C__")          
    def tearDown(self):
            print("tearDown_C")          

    def testOne(self):
        print ("C1")
        # test code
        pass

    def testTwo(self):
        print ("C2")
        # test code
        pass

if __name__ == '__main__':
    # Run only the tests in the specified classes

#    test_classes_to_run = [TestClassA, TestClassC, User_TestCase]
    test_classes_to_run = [TestClassA, TestClassC, User_TestCase,Book_TestCase]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)



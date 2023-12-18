import unittest
import HtmlTestRunner
import time
from utility.chrome import driver
from pageObjects.loginPage import loginPage

class loginTest(unittest.TestCase):
    baseurl="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def test_validlogin(self):
        #To create object for loginPage
        username = "Admin"
        password = "admin123"
        lp=loginPage(self.baseurl)
        lp.login(username, password)
        time.sleep(5)
        # self.assertEqual("dashboard/index",self.driver.title,"webpage title NOT matching")

    def test_invalidlogin(self):
        #To create object for loginPage
        username = "Admn"
        password = "admn123"
        lp=loginPage(self.baseurl)
        lp.invalidlogin(username, password)
        time.sleep(5)

    def test_emptylogin(self):
        #To create object for loginPage
        lp=loginPage(self.baseurl)
        lp.emptylogin()
        time.sleep(5)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()


if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\reports"))
import unittest
import HtmlTestRunner
from parameterized import parameterized
import os
import sys

__dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(__dir)
from src.loginPage import loginPage


__dir = os.path.dirname(os.path.realpath(__file__))
report_dir = os.path.join(os.path.dirname(os.path.realpath(__dir)), "report")


class TestLogin(unittest.TestCase):
    baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def test_valid_login(self):
        # To create object for loginPage
        username = "Admin"
        password = "admin123"
        lp = loginPage(self.baseurl)
        lp.login(username, password)
        assert lp.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    @parameterized.expand([("UserAdmin1", "passadmin"), ("UserAdmin2", "passadmin2")])
    def test_invalid_login(self, username_, password_):
        lp = loginPage(self.baseurl)
        res = lp.login(username_, password_)
        assert res == 'Invalid credentials'

    def test_empty_login(self):
        lp = loginPage(self.baseurl)
        res = lp.login(' ', ' ')
        assert res == 'Username and password is Required'


def Suite():

    # define a unit test container
    suiteTest = unittest.TestSuite()

    # add test cases to the container
    suiteTest.addTest(TestLogin("test_empty_login"))
    suiteTest.addTest(TestLogin("test_invalid_login"))
    suiteTest.addTest(TestLogin("test_valid_login"))
    return suiteTest


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_dir))

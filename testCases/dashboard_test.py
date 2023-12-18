import unittest
import HtmlTestRunner
import time

from pageObjects.loginPage import loginPage
from utility.chrome import driver

from pageObjects.Dashboard import Dashboard_Page

class dashboard_test(unittest.TestCase):
    baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def test_timeatwork(self):
        username = "Admin"
        password = "admin123"
        lp = loginPage(self.baseurl)
        lp.login(username, password)
        time.sleep(5)
        dp=Dashboard_Page(lp.driver).time_atwork()
        assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchIn'

    def test_assignleave(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            time.sleep(5)
            dp = Dashboard_Page(lp.driver).assignleave()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/assignLeave'

    def test_leave_list(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            time.sleep(5)
            dp = Dashboard_Page(lp.driver).leave_list()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList'

    def timesheets(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            time.sleep(5)
            dp = Dashboard_Page(lp.driver).timesheets()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet'

    def apply_leave(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            time.sleep(5)
            dp = Dashboard_Page(lp.driver).apply_leave()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/applyLeave'

    def my_leave(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            time.sleep(5)
            dp = Dashboard_Page(lp.driver).my_leave()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList'

    def my_timesheet(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            time.sleep(5)
            dp = Dashboard_Page(lp.driver).my_timesheet()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/time/viewMyTimesheet'


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\reports"))

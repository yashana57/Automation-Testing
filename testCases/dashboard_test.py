import unittest
import time
import os
import HtmlTestRunner
import sys

__dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(__dir)
from src.loginPage import loginPage
from src.Dashboard import Dashboard_Page

__dir = os.path.dirname(os.path.realpath(__file__))
report_dir = os.path.join(os.path.dirname(os.path.realpath(__dir)), "report")


class TestDashboard(unittest.TestCase):
    baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def test_time_at_work(self):
        username = "Admin"
        password = "admin123"
        lp = loginPage(self.baseurl)
        lp.login(username, password)
        dp = Dashboard_Page(lp.driver).time_atwork()
        assert dp == 'Punch Out' or 'Punch In'

    # @unittest.skip("This is a skipped test.")
    def test_assign_leave(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            dp = Dashboard_Page(lp.driver).assign_leave()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/assignLeave'

    # @unittest.skip("This is a skipped test.")
    def test_leave_list(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            time.sleep(5)
            dp = Dashboard_Page(lp.driver).leave_list()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList'

    # @unittest.skip("This is a skipped test.")
    def test_time_sheets(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            time.sleep(5)
            dp = Dashboard_Page(lp.driver).timesheets()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet'

    # @unittest.skip("This is a skipped test.")
    def test_apply_leave(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            time.sleep(5)
            dp = Dashboard_Page(lp.driver).apply_leave()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/applyLeave'

    # @unittest.skip("This is a skipped test.")
    def test_my_leave(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            time.sleep(5)
            dp = Dashboard_Page(lp.driver).my_leave()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewMyLeaveList'

    # @unittest.skip("This is a skipped test.")
    def test_my_timesheet(self):
            username = "Admin"
            password = "admin123"
            lp = loginPage(self.baseurl)
            lp.login(username, password)
            time.sleep(5)
            dp = Dashboard_Page(lp.driver).my_timesheet()
            assert dp == 'https://opensource-demo.orangehrmlive.com/web/index.php/time/viewMyTimesheet'


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=report_dir))
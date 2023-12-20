from selenium.webdriver.common.by import By
import time


class Dashboard_Page():
    Timeatwork_button='//button[@class="oxd-icon-button oxd-icon-button--solid-main orangehrm-attendance-card-action"]'
    assign_leavebutton='//button[@title="Assign Leave"]'
    leave_listbutton='//button[@title="Leave List"]'
    timesheetsbutton='//button[@title="Timesheets"]'
    apply_leavebutton='//button[@title="Apply Leave"]'
    my_leavebutton='//button[@title="My Leave"]'
    my_timesheetbutton='//button[@title="My Timesheet"]'
    time_header = "//div[@class='oxd-layout-context']/div/div/h6"

    def __init__(self, driver):
        self.driver = driver

    def time_atwork(self):
        self.driver.find_element(By.XPATH, self.Timeatwork_button).click()
        time.sleep(5)
        return self.driver.find_element('xpath', self.time_header).text

    def assign_leave(self):
        self.driver.find_element('xpath', self.assign_leavebutton).click()
        time.sleep(5)
        return self.driver.current_url

    def leave_list(self):
        self.driver.find_element('xpath', self.leave_listbutton).click()
        time.sleep(5)
        return self.driver.current_url

    def timesheets(self):
        self.driver.find_element('xpath', self.timesheetsbutton).click()
        time.sleep(5)
        return self.driver.current_url

    def apply_leave(self):
        self.driver.find_element('xpath', self.apply_leavebutton).click()
        time.sleep(5)
        return self.driver.current_url

    def my_leave(self):
        self.driver.find_element('xpath', self.my_leavebutton).click()
        time.sleep(5)
        return self.driver.current_url

    def my_timesheet(self):
        self.driver.find_element('xpath', self.my_timesheetbutton).click()
        time.sleep(5)
        return self.driver.current_url

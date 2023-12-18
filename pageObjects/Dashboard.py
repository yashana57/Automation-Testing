from selenium.webdriver.common.by import By
import time
from utility.chrome import driver


class Dashboard_Page():
    Timeatwork_button='//button[@class="oxd-icon-button oxd-icon-button--solid-main orangehrm-attendance-card-action"]'
    assign_leave='//button[@title="Assign Leave"]'
    leave_list='//button[@title="Leave List"]'
    timesheets='//button[@title="Timesheets"]'
    apply_leave='//button[@title="Apply Leave"]'
    my_leave='//button[@title="My Leave"]'
    my_timesheet='//button[@title="My Timesheet"]'

    def __init__(self, driver):
        self.driver = driver
    def time_atwork(self):
        self.driver.find_element(By.XPATH, self.Timeatwork_button).click()
        time.sleep(5)
        return self.driver.current_url
    def assignleave(self):
        self.driver.find_element(By.XPATH, self.assign_leave).click()
        time.sleep(5)
        return self.driver.current_url

    def leave_list(self):
        self.driver.find_element(By.XPATH, self.leave_list).click()
        time.sleep(5)
        return self.driver.current_url

    def timesheets(self):
        self.driver.find_element(By.XPATH, self.timesheets).click()
        time.sleep(5)
        return self.driver.current_url

    def apply_leave(self):
        self.driver.find_element(By.XPATH, self.apply_leave).click()
        time.sleep(5)
        return self.driver.current_url

    def my_leave(self):
        self.driver.find_element(By.XPATH, self.my_leave).click()
        time.sleep(5)
        return self.driver.current_url

    def my_timesheet(self):
        self.driver.find_element(By.XPATH, self.my_timesheet).click()
        time.sleep(5)
        return self.driver.current_url


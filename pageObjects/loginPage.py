from selenium.webdriver.common.by import By
from utility.chrome import driver
class loginPage():
    #locators of all page elements i.e. required
    textbox_username='//input[@name="username"]'
    textbox_password='//input[@name="password"]'
    button_login_xpath="//button[@type='submit']"
    err_msg='//div[@class="oxd-alert-content oxd-alert-content--error"]'
    def __init__(self,baseurl):
        self.driver = driver(baseurl)

    def login(self,username,password):
        self.driver.find_element('xpath', self.textbox_username).send_keys(username)
        self.driver.find_element('xpath',self.textbox_password).send_keys(password)
        self.driver.find_element('xpath', self.button_login_xpath).click()

    def invalidlogin(self,username,password):
        self.driver.find_element('xpath', self.textbox_username).send_keys(username)
        self.driver.find_element('xpath',self.textbox_password).send_keys(password)
        self.driver.find_element('xpath', self.button_login_xpath).click()
        return self.driver.find_element('xpath', self.err_msg).text
    def emptylogin(self):
        self.driver.find_element('xpath', self.button_login_xpath).click()
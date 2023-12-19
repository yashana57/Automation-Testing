
from utility.chrome import driver


class loginPage():
    # locators of all page elements i.e. required
    textbox_username = '//input[@name="username"]'
    textbox_password = '//input[@name="password"]'
    button_login_xpath = "//button[@type='submit']"
    err_msg = "//div[@class='oxd-alert-content oxd-alert-content--error']"
    required = "//div[@class='oxd-input-group oxd-input-field-bottom-space']/span"

    def __init__(self, baseurl):
        self.driver = driver(baseurl)

    def login(self, username, password):
        self.driver.find_element('xpath', self.textbox_username).send_keys(username)
        self.driver.find_element('xpath', self.textbox_password).send_keys(password)
        self.driver.find_element('xpath', self.button_login_xpath).click()
        msg = self.check_error_messages()
        self.driver.implicitly_wait(10)
        return msg

    def check_error_messages(self):
        error = self.driver.find_elements('xpath', self.err_msg)
        required = self.driver.find_elements('xpath', self.required)
        if len(error) != 0:
            error_msg = error[0].text
            return error_msg
        elif len(required) != 0:
            req_msg = 'Username and password is '+required[0].text
            return req_msg
        else:
            return

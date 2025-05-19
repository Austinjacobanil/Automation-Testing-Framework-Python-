from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from atHelper.selenium_helper import Selenium_Helper


class LoginPage(Selenium_Helper):

    email_webelement = (By.XPATH, "//input[@name='username']")
    password_webelement = (By.XPATH, "//input[@name='password']")
    login_webelement = (By.XPATH, "//button")


    def __init__(self, driver):
        super().__init__(driver)


    def login(self,username,password):
        self.webelements_enter(self.email_webelement, username)
        self.webelements_enter(self.password_webelement, password)
        self.webelements_click(self.login_webelement)


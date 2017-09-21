from selenium.webdriver.common.by import By
import time
from base.SeleniumDriver import SeleniumDriver
import Utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginClass(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    # locators identifiers
    _login_link= "Login"
    _email_field= "user_email"
    _password_field="user_password"
    _login_button="commit"


    # methods for performing actions on elements

    def clickLoginLink(self):
        self.elementClick(self._login_link,locatorType="link")

    def enterEmail(self,email):
        self.sendKeys(email,self._email_field,locatorType="id")

    def enterPassword(self,password):
        self.sendKeys(password,self._password_field,locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button,locatorType="name")



    # Functionnality which wraps all the actions needed to be performed on the page class

    def Login(self,email="",password=""):
        self.clickLoginLink()
        time.sleep(3)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccess(self):
        result = self.isElementPresent(".//div[@id='navbar']//span[text()='User Settings']", locatorType="xpath")
        return result

    def verifyLoginFail(self):
        result = self.isElementPresent("//div[contains(text(),'Invalid email or password')]", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Let's Kode It")




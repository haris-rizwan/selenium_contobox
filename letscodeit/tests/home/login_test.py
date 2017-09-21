from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.home.login_page import LoginClass
import unittest
import pytest
from Utilities.teststatus import TestStatus


@pytest.mark.usefixtures("OnetimesetUp","setUp")
class loginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self, OnetimesetUp):
        driver  =self.driver
        self.lP = LoginClass(driver)
        self.ts = TestStatus(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lP.Login("test@email.com","abcabc")
        time.sleep(3)
        result1 = self.lP.verifyLoginTitle()
        self.ts.mark(result1,"Title verification")
        result2=self.lP.verifyLoginSuccess()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")

        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_InvalidLogin(self):
        self.lP.Login("test@email.com","abcacabcu")

        time.sleep(3)

        result=self.lP.verifyLoginFail()

        assert result == True




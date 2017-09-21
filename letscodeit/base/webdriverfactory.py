"""
this factory file will generate a driver instance for us depending upon the the input
that we will get for the driver request

"""
from selenium import webdriver
import os

class WebDriverFactory():
    def __init__(self,browser):
        self.browser = browser

    def getWebDriverInstance(self):

        # it will get the driver instace based on the browser configuration

        baseURL = "https://letskodeit.teachable.com/"


        if self.browser == "firefox":
            driver = webdriver.Firefox()

        elif self.browser == "chrome":
            driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
            os.environ["chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
            print("Run test on chrome")

        else:
            driver = webdriver.Firefox()

        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get(baseURL)

        return driver

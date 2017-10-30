from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import os
from browsermobproxy import Server
import json
import urllib.request
import pandas as pd




capabilities = DesiredCapabilities.CHROME
capabilities['loggingPrefs'] = {'browser': 'DEBUG'}
capabilities['loggingPrefs'] = {'performance': 'ALL'}
capabilities['perfLoggingPrefs'] = {'enableTimeline': 'true'}


driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation
chrome_options = Options()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(driverLocation,desired_capabilities=capabilities)
driver.implicitly_wait(10)
driver.maximize_window()
baseUrl="www.google.com"
driver.get(baseUrl)

#using pandas to create a dataframe of the log.


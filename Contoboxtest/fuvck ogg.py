from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import json
import os
import pandas as pd
import re
import operator
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




server = Server('/Users/harisrizwan/SeleniumEnv/browsermob-proxy-2.1.4/bin/browsermob-proxy')
server.start()
proxy = server.create_proxy()


driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation

chrome_options = Options()
chrome_options.add_argument("headless")
chrome_options.add_argument(f'--proxy-server={proxy.proxy}')
driver = webdriver.Chrome(driverLocation,chrome_options=chrome_options)

# profile = webdriver.FirefoxProfile()
# profile.set_proxy(proxy.selenium_proxy())
#
# driver = webdriver.Firefox(firefox_profile=profile)

#
# capabilities = DesiredCapabilities.CHROME
#
# capabilities['proxy'] = {
#     'httpProxy' :'proxy' ,
#     'ftpProxy' : 'proxy',
#     'sslProxy' : 'proxy',
#     'noProxy' : None,
#     'proxyType' : "autodetect",
#     'class' : "org.openqa.selenium.Proxy",
#     'autodetect' : True
# }
#
# proxy.add_to_capabilities(capabilities)


driver.get('http://dbb1.contobox.com/v3/preview.php?id=18877')


time.sleep(6)
driver.save_screenshot("1.png")

print("hello")

driver.quit()
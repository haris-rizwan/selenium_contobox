from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import os

capabilities = DesiredCapabilities.CHROME
capabilities['loggingPrefs'] = {'browser':'DEBUG' }

driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation
chrome_options = Options()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(driverLocation,chrome_options=chrome_options,desired_capabilities=capabilities)
driver.implicitly_wait(10)
driver.maximize_window()
driver.set_window_position(0,22)
driver.set_window_size(1280,800)

# driver = webdriver.Chrome(desired_capabilities=capabilities)

driver.get('http://dbb1.contobox.com/v3/preview.php?id=16720')


driver.switch_to.frame(0)
banner=driver.find_element(By.ID,"cb-ctr")
banner.click()
print("Pre banner clicked")

driver.implicitly_wait(10)

# print console log messages
for entry in driver.get_log('browser'):
    print(entry)

# desired_capabilities=capabilities,
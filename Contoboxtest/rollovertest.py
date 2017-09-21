from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from  selenium.webdriver import ActionChains


#15128
#14517 chervolt
#14240
#14534 dorothy
#15472
#15455 ford q3
#15472 kohler
#15115 TROJ

baseUrl = "https://srv1.contobox.com/v3/preview.php?id=15472"
# baseUrl = "http://dbb1.contobox.com/v3/preview.php?id=15503"

# WEb driver call

driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation)
driver.implicitly_wait(10)
driver.maximize_window()
driver.set_window_position(0,22)
driver.set_window_size(1280,800)
# print(position)
driver.get(baseUrl)



driver.switch_to.frame(0)
banner=driver.find_element(By.ID,"cb-ctr")
time.sleep(3)
actions =ActionChains(driver)
actions.move_to_element(banner).perform()
print("Rollover mouse complete")

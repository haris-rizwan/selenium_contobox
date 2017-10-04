from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import os
import urllib.request
import pandas as pd
from openpyxl import workbook
from openpyxl import worksheet




capabilities = DesiredCapabilities.CHROME
capabilities['loggingPrefs'] = {'browser':'ALL' }
capabilities['loggingPrefs'] = {'performance':'ALL' }

driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation
chrome_options = Options()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(driverLocation,chrome_options=chrome_options,desired_capabilities=capabilities)
driver.implicitly_wait(10)
driver.maximize_window()
driver.set_window_position(0,22)
driver.set_window_size(1280,800)
baseUrl ='file:///Users/harisrizwan/Desktop/test/ToDO%20list/index.html'
# driver = webdriver.Chrome(desired_capabilities=capabilities)
# http://dbb1.contobox.com/v3/preview.php?id=16720
driver.get(baseUrl)

# file:///Users/harisrizwan/Desktop/test/ToDO%20list/index.html



# driver.switch_to.frame(0)
# banner=driver.find_element(By.ID,"cb-ctr")
# banner.click()
# print("Pre banner clicked")
#
# driver.implicitly_wait(10)





# print console log messages

#all the log entries every single entry is in form of a dictionary object.

# entry = driver.get_log('browser')
# print(entry)
# for i in entry:
#     print(entry.keys())

# for entry in driver.get_log('browser'):
#     # if entry.level == "WARNING":
#     #     print("it works")
#     print(entry.keys())
#
#     for key, value in entry.items():
#         if "WARNING" == value:
#             print ("Here is the log =  " + entry["message"])




msg = pd.DataFrame(driver.get_log('browser'))


dfstatus= msg[msg['level'].str.contains("SEVERE")]

if dfstatus is not None:
    writer = pd.ExcelWriter('/Users/harisrizwan/ID+_+Time.xlsx')
    dfstatus.to_excel(writer,'sheet1',index=False)
    writer.save()
    print(dfstatus)


dfstatus.to_clipboard(index=False)











# desired_capabilities=capabilities,

# for value in driver.get_log('performance'):
#
#     print(value)

# value = driver.get_log('performance')
# print(value)

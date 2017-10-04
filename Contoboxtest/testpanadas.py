from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time
from openpyxl import workbook
from openpyxl import worksheet
from selenium.webdriver.chrome.options import Options
import os
import urllib.request
import pandas as pd

capabilities = DesiredCapabilities.CHROME
capabilities['loggingPrefs'] = {'browser': 'DEBUG'}
capabilities['loggingPrefs'] = {'performance': 'ALL'}

driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation
chrome_options = Options()
chrome_options.add_argument("headless")
driver = webdriver.Chrome(driverLocation, chrome_options=chrome_options, desired_capabilities=capabilities)
driver.implicitly_wait(10)
driver.maximize_window()
driver.set_window_position(0, 22)
driver.set_window_size(1280, 800)
baseUrl = 'http://dbb1.contobox.com/v3/preview.php?id=17086'
# driver = webdriver.Chrome(desired_capabilities=capabilities)
# http://dbb1.contobox.com/v3/preview.php?id=16720
driver.get(baseUrl)

driver.switch_to.frame(0)
banner = driver.find_element(By.ID, "cb-ctr")
banner.click()
print("Pre banner clicked")

driver.implicitly_wait(10)

# print console log messages

# all the log entries every single entry is in form of a dictionary object.

# entry = driver.get_log('browser')
# print(entry)
# for i in entry:
#     print(entry.keys())

for entry in driver.get_log('browser'):
    # if entry.level == "WARNING":
    #     print("it works")
    print(entry.keys())

    for key, value in entry.items():
        if "WARNING" == value:
            print("Here is the log =  " + entry["message"])

# desired_capabilities=capabilities,

df = pd.DataFrame(driver.get_log('performance')) ###creating a dataframe on pandas having 3 collumns : level, message and timestamp

# dfnetworkonly = df[df['message'].str.contains("Network")] ###creating a NEW dataframe,base on df, BUT having only rows with the word "Network" in the message line.
# dfnetworkonly2 = dfnetworkonly[dfnetworkonly['message'].str.contains("Network.loadingFinished")] ###creating a NEW dataframe,base on dfnetworkonly, BUT having only rows where the word "Network.loadingFinished" is in the row.


dfstatus= df[df['message'].str.contains("Network")]
dfstatus2=dfstatus[dfstatus['message'].str.contains('"status":200,"statusText":"OK"')]


print(dfstatus2)

dfstatus2.to_clipboard(index=False)

# dfnetworkonly2.to_clipboard(index=False) ##export to clipboard (copy paste)
#dfnetworkonly2.to_csv('/Users/alain/Desktop/working/result.csv',index=False) #export to csv

#writer = pd.ExcelWriter('/Users/alain/Documents/excelfile.xlsx')
#dfnetworkonly2.to_excel(writer,'Sheet1',index=False)
#writer.save() #export to excel

#for value in driver.get_log('performance'):

    #print(value)

    # value = driver.get_log('performance')
    # print(value)
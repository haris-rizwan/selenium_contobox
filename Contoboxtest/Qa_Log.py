from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import os
import urllib.request
import pandas as pd
import datetime
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


Add_id =str(17831)


baseUrl = 'http://dbb1.contobox.com/v3/preview.php?id='+Add_id

driver.get(baseUrl)



msg = pd.DataFrame(driver.get_log('browser'))

print(msg)
dfstatus= msg[msg['level'].str.contains("SEVERE")]

print(dfstatus)

if dfstatus.empty:
    print("No errors")

else:
    x = dfstatus.iloc[0]['timestamp']
    # y = time.ctime(int(x) / 1000)
    y = str(datetime.datetime.strptime(time.ctime(int(x) / 1000 ), "%a %b %d %H:%M:%S %Y"))
    print(y)
    writer = pd.ExcelWriter('/Users/harisrizwan/'+Add_id+'_'+y+'.xlsx')
    dfstatus.to_excel(writer,'sheet1',index=False)
    writer.save()
    print(dfstatus)


dfstatus.to_clipboard(index=False)


driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os



baseUrl = "https://srv1.contobox.com/v3/preview.php?id=14517"

# WEb driver call

driver = webdriver.Safari()
driver.implicitly_wait(10)
driver.get(baseUrl)
size= driver.get_window_size()
print(size)
handle =driver.current_window_handle
print(handle)
x, y = 0,22

width = 2560
height = 1440

cmd = "osascript -e 'tell application \"Safari\" to set bounds of front window to {%d, %d, %d, %d}'" \
          % (x, y, width+x, height+y)
os.system(cmd)

def tabpresent():

    try:
        tabs = driver.find_elements(By.ID,"banner")
        if len(tabs)>0:
            print(Len(tabs))

        else:
            print("element no available")

    except:
        print("element not found")



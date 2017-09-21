from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import time
import os
from selenium.webdriver.chrome.options import Options

#15128
#14517 chervolt
#14240
#14534 dorothy
#15472
#15455 ford q3
#15472 kohler
#15115 TROJ

# baseUrl = "https://srv1.contobox.com/v3/preview.php?id=15819"
baseUrl = "http://dbb1.contobox.com/v3/preview.php?id=14534"

# WEb driver call

driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation
chrome_options = Options()
chrome_options.add_argument("headless")
chrome_options.add_argument('window-size=1280x800')
driver = webdriver.Chrome(driverLocation,chrome_options=chrome_options)
driver.implicitly_wait(10)
driver.get(baseUrl)



def waitForElement(locatorType,locator, timeout=10, pollFrequency=0.5):
    element = None
    try:
        wait = WebDriverWait(driver, timeout=timeout,
                             poll_frequency=pollFrequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        # element = wait.until(EC.element_to_be_clickable((locator,locatorType)))
        element = wait.until(EC.visibility_of_element_located((locatorType,locator)))

        print("Element appeared on the web page")
    except:
        print("Element not appeared on the web page")

    return element


def waitForElements(locatorType,locator, timeout=10, pollFrequency=0.5):
    elements = None
    try:
        wait = WebDriverWait(driver, timeout=timeout,
                             poll_frequency=pollFrequency,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        # elements = wait.until(EC.element_to_be_clickable((locatorType,locator)))
        # elements = wait.until(EC.presence_of_all_elements_located((locatorType,locator)))

        elements = wait.until(EC.visibility_of_all_elements_located((locatorType,locator)))

        print("Elements appeared on the web page")
    except:
        print("Elements not appeared on the web page")

    return elements

driver.switch_to.frame(0)

banner = waitForElement(By.ID,"cb-ctr")
# banner=driver.find_element(By.ID,"cb-ctr")

print(banner)

actions =ActionChains(driver)
actions.move_to_element(banner).perform()
print("Rollover mouse complete")

wait = WebDriverWait(driver,10,0.5,ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException,
                                                       NoSuchFrameException,NoSuchWindowException])

driver.switch_to.default_content()
print("content switched")
switch = wait.until(EC.frame_to_be_available_and_switch_to_it(1))
print("switched to frame 1")

mainpage=driver.current_window_handle

time.sleep(4)

driver.save_screenshot("1.png")


#Check which elements are present

def ElementPresent(LocatorType,Locator):

    try:
        elements = driver.find_elements(LocatorType,Locator)
        if len(elements)>0:
            print(len(elements))
            return True

        else:
            print("element no available")
            return False

    except:
        print("element not found")
        return False




social_Buttons = waitForElements(By.CLASS_NAME,"social-button")
print(len(social_Buttons))
print(social_Buttons)


# if social_Buttons is not None:
#     for i in social_Buttons:
#         if i.is_displayed():
#             i.click()
#             time.sleep(1)
#             driver.switch_to.window(mainpage)
#             driver.switch_to.default_content()
#             driver.switch_to.frame(1)
#         else:
#             print("Element no optically visible")
#
#
#
# #             for Headless chrome
if social_Buttons is not None:
    for i in social_Buttons:
        # actions.move_to_element(i)
        actions.click(i)
        print(i)
        time.sleep(1)
        driver.switch_to.window(mainpage)
        driver.switch_to.default_content()
        driver.switch_to.frame(1)
#
#
h = driver.window_handles
print(len(h))

shop = driver.find_element(By.ID,"component-button-1")
shop.click()
time.sleep(2)

driver.save_screenshot("2.png")

#
# for i in h:
#     num = h.index(i)
#     if num > 0:
#         print(num)
#         driver.switch_to.window(i)
#         time.sleep(1)
#         fileName = "SocialButton"+str(num)+".png"
#         print(fileName)
#         driver.save_screenshot(fileName)
#         time.sleep(1)
#
#
#
# for i in h:
#     num = h.index(i)
#     if num > 0:
#         print(i)
#         driver.switch_to.window(i)
#         driver.close()
#
#
#
# driver.switch_to.window(mainpage)
# driver.switch_to.default_content()
# driver.switch_to.frame(1)
#
#
driver.quit()

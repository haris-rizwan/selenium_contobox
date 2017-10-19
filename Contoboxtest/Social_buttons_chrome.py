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
baseUrl = "http://dbb1.contobox.com/v3/preview.php?id=15472"

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


###################### Social Buttons ########################################
#
social_Buttons = waitForElements(By.CLASS_NAME,"social-button")
print(len(social_Buttons))
print(social_Buttons)


if social_Buttons is not None:
    for i in social_Buttons:
        if i.is_displayed():
            i.click()
            time.sleep(1)
            driver.switch_to.window(mainpage)
            driver.switch_to.default_content()
            driver.switch_to.frame(1)
        else:
            print("Element not optically visible")

else:
    print("Social Buttons not present")



h = driver.window_handles

for i in h:
    num = h.index(i)
    if num > 0:
        print(num)
        driver.switch_to.window(i)
        time.sleep(1)
        fileName = "SocialButton"+str(num)+".png"
        print(fileName)
        driver.save_screenshot(fileName)
        time.sleep(1)



for i in h:
    num = h.index(i)
    if num > 0:
        print(i)
        driver.switch_to.window(i)
        driver.close()



driver.switch_to.window(mainpage)
driver.switch_to.default_content()
driver.switch_to.frame(1)

#################### Piano TAB ###################################

SocialShare = waitForElement(By.CLASS_NAME, "piano-button-0")

if SocialShare is not None:
    SocialShare.click()

    Piano_tab = waitForElement(By.CLASS_NAME, "component-frame-index-0 ")

    driver.save_screenshot("Social-share-tab" + ".png")

    Share_buttons = waitForElements(By.XPATH, ".//div[@class='share-buttons']//a")
    print(len(Share_buttons))

    if Share_buttons is not None:
        for i in Share_buttons:
            if i.is_displayed():
                i.click()
                time.sleep(1)
                driver.switch_to.window(mainpage)
                driver.switch_to.default_content()
                driver.switch_to.frame(1)
            else:
                print("Share Button not optically visible")

    h = driver.window_handles

    for i in h:
        num = h.index(i)
        if num > 0:
            print(num)
            driver.switch_to.window(i)
            time.sleep(1)
            fileName = "Share-Buttons" + str(num) + ".png"
            print(fileName)
            driver.save_screenshot(fileName)
            time.sleep(1)

    for i in h:
        num = h.index(i)
        if num > 0:
            print(i)
            driver.switch_to.window(i)
            driver.close()

    driver.switch_to.window(mainpage)
    driver.switch_to.default_content()
    driver.switch_to.frame(1)

    #####################Share Icons#################################

    Share_Icons = driver.find_elements(By.XPATH, ".//div[@class='share-icons']//a")
    print(len(Share_Icons))

    if Share_Icons is not None:
        for i in Share_Icons:
            if i.is_displayed():
                i.click()
                time.sleep(1)
                driver.switch_to.window(mainpage)
                driver.switch_to.default_content()
                driver.switch_to.frame(1)
            else:
                print("Share Icon not optically visible")

    h = driver.window_handles

    for i in h:
        num = h.index(i)
        if num > 0:
            print(num)
            driver.switch_to.window(i)
            time.sleep(1)
            fileName = "Share-Icons" + str(num) + ".png"
            print(fileName)
            driver.save_screenshot(fileName)
            time.sleep(1)

    for i in h:
        num = h.index(i)
        if num > 0:
            print(i)
            driver.switch_to.window(i)
            driver.close()

    driver.switch_to.window(mainpage)
    driver.switch_to.default_content()
    driver.switch_to.frame(1)

else:
    print("Social Share Tab is not present")



driver.quit()



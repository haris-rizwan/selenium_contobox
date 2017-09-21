from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.by import By
from  selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
#15128
#14517 chervolt
#14240
#14534 dorothy

baseUrl = "https://srv1.contobox.com/v3/preview.php?id=14517"

# WEb driver call
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
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
        # element = wait.until(EC.element_to_be_clickable((locator,locatorType)))
        elements = wait.until(EC.visibility_of_all_elements_located((locatorType,locator)))

        print("Element appeared on the web page")
    except:
        print("Element not appeared on the web page")

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

# Store the main window handle for future reference

mainpage=driver.current_window_handle



tabs = driver.find_elements(By.CSS_SELECTOR,".tab-button")
# tabs = driver.find_elements(By.XPATH,".//div[@id='layout-tabs']/div")

print("There are "+ str(len(tabs)) + " tabs in this Contobox")


k = 1
if tabs is not None:
    for i in tabs:
        i.click()
        time.sleep(2)
        driver.save_screenshot("Tab"+str(k)+".png")
        k += 1
        # time.sleep(2)


# find all the CTAs

LinksCTA = driver.find_elements(By.XPATH,".//div[@id='custom-links']/a")
print("There are "+ str(len(LinksCTA)) + " CTAs in this Contobox")



if LinksCTA is not None:
    for i in LinksCTA:
        if i.is_displayed():
            i.click()
            time.sleep(2)
            driver.switch_to.window(mainpage)
            time.sleep(2)
            driver.switch_to.default_content()
            driver.switch_to.frame(1)
            # driver.switch_to.frame(1)
        else:
            print("Element no optically visible")


h = driver.window_handles

for i in h:
    num = h.index(i)
    if num > 0:
        print(num)
        driver.switch_to.window(i)
        time.sleep(1)
        fileName = "CTA"+str(num)+".png"
        print(fileName)
        driver.save_screenshot(fileName)
        time.sleep(1)
        # driver.switch_to.window(mainpage)
        # driver.switch_to.frame(1)
        # time.sleep(2)


for i in h:
    num = h.index(i)
    if num > 0:
        print(i)
        driver.switch_to.window(i)
        driver.close()
        # driver.switch_to.window(mainpage)
        # driver.switch_to.frame(1)
        time.sleep(1)






driver.switch_to.window(mainpage)
driver.switch_to.default_content()
driver.switch_to.frame(1)

#find all the Social button
SocialButtons = driver.find_elements(By.CLASS_NAME,"social-button")
print("There are "+ str(len(SocialButtons)) + " Social Buttons in this Contobox")

if SocialButtons is not None:
    for i in SocialButtons:
        if i.is_displayed():
            i.click()
            time.sleep(1)
            driver.switch_to.window(mainpage)
            driver.switch_to.default_content()
            driver.switch_to.frame(1)
        else:
            print("Element no optically visible")


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
        # driver.switch_to.window(mainpage)
        # driver.switch_to.frame(1)
        # time.sleep(2)


for i in h:
    num = h.index(i)
    if num > 0:
        print(i)
        driver.switch_to.window(i)
        driver.close()
        # driver.switch_to.window(mainpage)
        # driver.switch_to.frame(1)
        # time.sleep(2)


driver.switch_to.window(mainpage)
driver.switch_to.default_content()
driver.switch_to.frame(1)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from  selenium.webdriver import ActionChains
#15128
#14517 chervolt
#14240
#14534 dorothy
#15472 kohler
#15455 ford
#15505
baseUrl = "https://srv1.contobox.com/v3/preview.php?id=15472"


# WEb driver call

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(baseUrl)

time.sleep(3)

# Store the main window handle for future reference

mainpage=driver.current_window_handle


#Pre banner expansion click
driver.switch_to.frame(0)
banner=driver.find_element(By.CLASS_NAME,"banner")
time.sleep(2)
actions =ActionChains(driver)
actions.move_to_element(banner).perform()
print("Rollover mouse complete")
print("Pre banner clicked")

time.sleep(4)

#Move over to the expanded iframe
driver.switch_to.default_content()
driver.switch_to.frame(1)


time.sleep(3)

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

Tabs = ElementPresent(By.CSS_SELECTOR,".tab-button")
# Tabs = ElementPresent(By.XPATH,".//div[@id='layout-tabs']/div")
LinksCTA = ElementPresent(By.XPATH,".//div[@id='custom-links']/a")
SocialButtons = ElementPresent(By.CLASS_NAME,"social-button")
SocialShare = ElementPresent(By.ID,"component-button-3")




if Tabs:
    tabs = driver.find_elements(By.CSS_SELECTOR,".tab-button")

    print("There are " + str(len(tabs)) + " tabs in this Contobox")

    k = 1
    if tabs is not None:
        for i in tabs:
            i.click()
            time.sleep(2)
            driver.save_screenshot("Tab" + str(k) + ".png")
            k += 1
            # time.sleep(2)

else:
    print("No Tabs available")


if LinksCTA:
    CTA = driver.find_elements(By.XPATH, ".//div[@id='custom-links']/a")
    print("There are " + str(len(CTA)) + " CTAs in this Contobox")

    if LinksCTA is not None:
        for i in CTA:
            if i.is_displayed():
                i.click()
                time.sleep(2)
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
            fileName = "CTA" + str(num) + ".png"
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


else:
    print("No CTA available")


#Switch to main content

driver.switch_to.window(mainpage)
driver.switch_to.default_content()
driver.switch_to.frame(1)


if SocialButtons:
    Buttons = driver.find_elements(By.CLASS_NAME, "social-button")
    print("There are " + str(len(Buttons)) + " Social Buttons in this Contobox")

    if SocialButtons is not None:
        for i in Buttons:
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
            fileName = "SocialButton" + str(num) + ".png"
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


if SocialShare:
    SocialShare = driver.find_element(By.ID, "component-button-3")
    SocialShare.click()
    time.sleep(2)
    driver.save_screenshot("Social-share-tab" +".png")
    Share_buttons = driver.find_elements(By.XPATH,".//div[@class='share-buttons']//a")
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
                        print("Element not optically visible")

    h = driver.window_handles

    for i in h:
            num = h.index(i)
            if num > 0:
                print(num)
                driver.switch_to.window(i)
                time.sleep(1)
                fileName = "Share-Button " + str(num) + ".png"
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


    #Switch to main content

    driver.switch_to.window(mainpage)
    driver.switch_to.default_content()
    driver.switch_to.frame(1)


    Share_icons = driver.find_elements(By.XPATH,".//div[@class='share-icons']//a")
    print(len(Share_icons))
    if Share_icons is not None:
        for i in Share_icons:
            if i.is_displayed():
                    i.click()
                    time.sleep(1)
                    driver.switch_to.window(mainpage)
                    driver.switch_to.default_content()
                    driver.switch_to.frame(1)

            else:
                    print("Element not optically visible")

    h = driver.window_handles

    for i in h:
        num = h.index(i)
        if num > 0:
            print(num)
            driver.switch_to.window(i)
            time.sleep(1)
            fileName = "Share-Icons " + str(num) + ".png"
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

    # Switch to main content

    driver.switch_to.window(mainpage)
    driver.switch_to.default_content()
    driver.switch_to.frame(1)

    Piano_back =driver.find_element(By.CLASS_NAME,"piano-back")
    Piano_back.click()
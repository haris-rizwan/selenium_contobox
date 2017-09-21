from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
#15128
#14517
#14240
#14534

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

width = 1280
height = 800

cmd = "osascript -e 'tell application \"Safari\" to set bounds of front window to {%d, %d, %d, %d}'" \
          % (x, y, width+x, height+y)
os.system(cmd)

time.sleep(3)

# driver = webdriver.Firefox()
# driver.implicitly_wait(10)
# driver.maximize_window()
# driver.get(baseUrl)
#
# time.sleep(3)

# Store the main window handle for future reference

mainpage=driver.current_window_handle


#Pre banner expansion click
driver.switch_to.frame(0)
print("frame switched")
banner=driver.find_element(By.CLASS_NAME,"banner")
banner.click()
print("Pre banner clicked")

time.sleep(2)

#Move over to the expanded iframe
driver.switch_to.default_content()
driver.switch_to.frame(1)


time.sleep(2)
# find all the tab and click

tabs = driver.find_element(By.XPATH,".//li[@id='component-button-1']")
# tabs = driver.find_elements(By.XPATH,".//div[@id='layout-tabs']/div")

# print("There are "+ str(len(tabs)) + " tabs in this Contobox")
print(tabs)

tabs.click()
# k = 1
# if tabs is not None:
#     for i in tabs:
#         print(i)
#         i.click()
#         time.sleep(2)
#         driver.save_screenshot("Tab"+str(k)+".png")
#         k += 1
#         # time.sleep(2)


# find all the CTAs

# LinksCTA = driver.find_elements(By.XPATH,".//div[@id='custom-links']/a")
# print("There are "+ str(len(LinksCTA)) + " CTAs in this Contobox")
#
#
#
# if LinksCTA is not None:
#     for i in LinksCTA:
#         if i.is_displayed():
#             i.click()
#             time.sleep(2)
#             driver.switch_to.window(mainpage)
#             driver.switch_to.frame(1)
#         else:
#             print("Element no optically visible")

#
# h = driver.window_handles
#
# for i in h:
#     num = h.index(i)
#     if num > 0:
#         print(num)
#         driver.switch_to.window(i)
#         time.sleep(1)
#         fileName = "CTA"+str(num)+".png"
#         print(fileName)
#         driver.save_screenshot(fileName)
#         time.sleep(1)
#         # driver.switch_to.window(mainpage)
#         # driver.switch_to.frame(1)
#         # time.sleep(2)
#
#
# for i in h:
#     num = h.index(i)
#     if num > 0:
#         print(i)
#         driver.switch_to.window(i)
#         driver.close()
#         # driver.switch_to.window(mainpage)
#         # driver.switch_to.frame(1)
#         time.sleep(1)
#
#
#
#
#
#
# driver.switch_to.window(mainpage)
# driver.switch_to.frame(1)
#
# #find all the Social button
# SocialButtons = driver.find_elements(By.CLASS_NAME,"social-button")
# print("There are "+ str(len(SocialButtons)) + " Social Buttons in this Contobox")
#
# if SocialButtons is not None:
#     for i in SocialButtons:
#         if i.is_displayed():
#             i.click()
#             time.sleep(1)
#             driver.switch_to.window(mainpage)
#             driver.switch_to.frame(1)
#         else:
#             print("Element no optically visible")
#
#
# h = driver.window_handles
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
#         # driver.switch_to.window(mainpage)
#         # driver.switch_to.frame(1)
#         # time.sleep(2)
#
#
# for i in h:
#     num = h.index(i)
#     if num > 0:
#         print(i)
#         driver.switch_to.window(i)
#         driver.close()
#         # driver.switch_to.window(mainpage)
#         # driver.switch_to.frame(1)
#         # time.sleep(2)
#
#
# driver.switch_to.window(mainpage)
# driver.switch_to.frame(1)
#
# #social share
#
# SocialShare = driver.find_element(By.ID,"component-button-3")
# if SocialShare is not None:
#     print("Social share is present")
#
# # screenshot method
#     def screenShot(self, baseUrl):
#         """
#         Takes screenshot of the current open web page
#         """
#         fileName = baseUrl + "." + str(round(time.time() * 1000)) + ".png"
#         screenshotDirectory = "../screenshots/"
#         relativeFileName = screenshotDirectory + fileName
#         currentDirectory = os.path.dirname(__file__)
#         destinationFile = os.path.join(currentDirectory, relativeFileName)
#         destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
#
#         try:
#             if not os.path.exists(destinationDirectory):
#                 os.makedirs(destinationDirectory)
#             self.driver.save_screenshot(destinationFile)
#             self.log.info("Screenshot save to directory: " + destinationFile)
#         except:
#             self.log.error("### Exception Occurred when taking screenshot")
#             print_stack()
#



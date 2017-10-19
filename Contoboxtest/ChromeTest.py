from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
#15128
#14517 chervolt
#14240
#14534 dorothy

baseUrl = "https://srv1.contobox.com/v3/preview.php?id=15472"

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



# Store the main window handle for future reference

mainpage=driver.current_window_handle


#Pre banner expansion click
driver.switch_to.frame(0)
banner=driver.find_element(By.ID,"cb-ctr")
banner.click()
print("Pre banner clicked")

time.sleep(2)

#Move over to the expanded iframe
driver.switch_to.default_content()
driver.switch_to.frame(1)


time.sleep(2)
#find all the tab and click

# tabs = driver.find_elements(By.CSS_SELECTOR,".tab-button")
tabs = driver.find_elements(By.XPATH,".//div[@id='layout-tabs']/div")

print("There are "+ str(len(tabs)) + " tabs in this Contobox")

k = 1
if tabs is not None:
    for i in tabs:
        i.click()
        time.sleep(2)
        driver.save_screenshot("Tab"+str(k)+".png")
        k += 1
        # time.sleep(2)



# screenshot method
    def screenShot(self, baseUrl):
        """
        Takes screenshot of the current open web page
        """
        fileName = baseUrl + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")
            print_stack()




from selenium import webdriver
import os


driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation
driver = webdriver.Chrome(driverLocation)
driver.implicitly_wait(10)
driver.maximize_window()

source = "http://dbb1.contobox.com/v3/preview.php?id=17080"

driver.get(source)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart

print ("Back End: %s" % backendPerformance)
print ("Front End: %s" % frontendPerformance)

driver.quit()
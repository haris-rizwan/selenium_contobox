from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as expected
from selenium.webdriver.support.wait import WebDriverWait


options = Options()
options.add_argument('-headless')
driver = Firefox(firefox_options=options)
wait = WebDriverWait(driver, timeout=10)
driver.get('http://www.google.com')
wait.until(expected.visibility_of_element_located((By.NAME, 'q'))).send_keys('headless firefox' + Keys.ENTER)
wait.until(expected.visibility_of_element_located((By.CSS_SELECTOR, '#ires a'))).click()
print(driver.page_source)
driver.quit()
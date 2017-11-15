from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import json
import os
import pandas as pd
import re


#to Use browsermob proxy you have to install using pip and also install the binary file
#in setting up the server give the complete path to the install binnary browsermob-proxy

server = Server('/Users/harisrizwan/SeleniumEnv/browsermob-proxy-2.1.4/bin/browsermob-proxy')
server.start()
proxy = server.create_proxy()

driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation

options = Options()
options.add_argument(f'--proxy-server={proxy.proxy}')
driver = webdriver.Chrome(driverLocation, desired_capabilities=options.to_capabilities())




proxy.new_har()
driver.get('https://am.contobox.com/v3/preview.php?id=21423')

# http://dbb1.contobox.com/v3/preview.php?id=18232
#12734
# 18191

driver.switch_to.frame(0)
banner = driver.find_element(By.ID, "cb-ctr")
banner.click()
print("Pre banner clicked")

time.sleep(6)

result = json.dumps(proxy.har)
json_data = json.loads(result)






df = pd.DataFrame([x for x in json_data['log']['entries']])

# request= [x for x in json_data['log']['entries']]

df.to_clipboard(index=False)


y= df['request']
x = df['response']

http_check = len(y)


l=0

for i in range(0,http_check):
    # print(y[i]['url'])
    if re.match(reg,y[i]['url']):
        print ("found")
    else:
        print("all https")



Num_request = len(x)

# print("The Number of Request are {}".format(Num_request))


j = 0
for i in range(0,Num_request):
    # print(x[i]['headersSize'])
    j = j + x[i]['headersSize']
    print("header size {0} = {1}".format(i, j))

k = 0
for i in range(0,Num_request):
    # print(x[i]['bodySize'])
    k = k + x[i]['bodySize']
    print("body size {0} = {1}".format(i, k))


print("Total Header Size = {}".format(j))
print("Total Body Size = {}".format(k))
print("The Number of Request are {}".format(Num_request))
print("Total Transferred Size = {}kb (+/- 10kb)".format((j + k)/1000))
# df['headersSize'] = df['response'].str.split(",").str[-3].str[16:].astype(int)
# df['bodySize'] = df['response'].str.split(",").str[-2].str[13:].astype(int)

server.stop()
driver.close()
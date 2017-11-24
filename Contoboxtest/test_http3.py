from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import json
import os
import pandas as pd
import re
import operator
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#to Use browsermob proxy you have to install using pip and also install the binary file
#in setting up the server give the complete path to the install binnary browsermob-proxy

server = Server('/Users/harisrizwan/SeleniumEnv/browsermob-proxy-2.1.4/bin/browsermob-proxy')
server.start()
proxy = server.create_proxy()


#
# capabilities = DesiredCapabilities.CHROME
#
# capabilities['proxy'] = {
#     'httpProxy' :'proxy' ,
#     'ftpProxy' : 'proxy',
#     'sslProxy' : 'proxy',
#     'noProxy' : None,
#     'proxyType' : "autodetect",
#     'class' : "org.openqa.selenium.Proxy",
#     'autodetect' : True
# }
#
# proxy.add_to_capabilities(capabilities)

driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
os.environ["chrome.driver"] = driverLocation

chrome_options = Options()
# chrome_options.add_argument("headless")
chrome_options.add_argument(f'--proxy-server={proxy.proxy}')
# driver = webdriver.Chrome(driverLocation,desired_capabilities=chrome_options.to_capabilities())
driver = webdriver.Chrome(driverLocation,chrome_options=chrome_options)

# profile = webdriver.FirefoxProfile()
# profile.set_proxy(proxy.selenium_proxy())
#
# driver = webdriver.Firefox(firefox_profile=profile)




proxy.new_har()
driver.get('https://dbb1.contobox.com/v3/preview.php?id=18774')

# http://dbb1.contobox.com/v3/preview.php?id=18232
# https://am.contobox.com/v3/preview.php?id=21423
#12734
# 18191
#18877 emirates
#18729 toysrus
#18754

#18774 shen yu

time.sleep(3)


result = json.dumps(proxy.har)
json_data = json.loads(result)


df = pd.DataFrame([x for x in json_data['log']['entries']])

df.to_clipboard(index=False)

d = df['request']
v = df['response']

pre_http_check = len(d)
pre_Num_request = len(v)




pre_ListOfHttpURL = []
pre_ListOfHttpsURL = []

for i in range(0,pre_http_check):
    # print(y[i]['url'])
    w = re.findall(r"\b" + 'https://' + r"\b",d[i]['url'])
    # print(w)
    if "https://" in w:
        pre_ListOfHttpsURL.append(d[i]['url'])
    else:
        pre_ListOfHttpURL.append(d[i]['url'])


m = 0
n = 0


for i in range(0, pre_Num_request):
        # print(x[i]['headersSize'])
        m = m + v[i]['headersSize']
        n = n + v[i]['bodySize']
        # print("header size {0} = {1}".format(i, m))
        # print("body size {0} = {1}".format(i, n))




print("Total Header Size = {}".format(m))
print("Total Body Size = {}".format(n))
print("The Number of Request of Pre-Expandable are {}".format(pre_Num_request))
print("Number of Pre-Expandable Http URLs = " +str(len(pre_ListOfHttpURL)))
print("Number of Pre-Expandable Https URLs = " +str(len(pre_ListOfHttpsURL)))
print("Total Transferred Size of Pre-Expandable = {}kb (+/- 10kb)".format((m + n)/1000))


################################################################################################


print("###############***************##############************%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")




driver.get("https://dbb1.contobox.com/v3/preview.php?id=18774&tpl=preview_expanded")

time.sleep(6)

result = json.dumps(proxy.har)
json_data = json.loads(result)






df = pd.DataFrame([x for x in json_data['log']['entries']])


df.to_clipboard(index=False)


y= df['request']
x = df['response']

http_check = len(y)
Num_request = len(x)




ListOfHttpURL = []
ListOfHttpsURL = []

for i in range(0,http_check):
    # print(y[i]['url'])
    w = re.findall(r"\b" + 'https://' + r"\b",y[i]['url'])
    # print(w)
    if "https://" in w:
        ListOfHttpsURL.append(y[i]['url'])
    else:
        ListOfHttpURL.append(y[i]['url'])


j = 0
k = 0
sample_dic = {}
for i in range(0,Num_request):
    # print(x[i]['headersSize'])
    j = j + x[i]['headersSize']
    k = k + x[i]['bodySize']
    var1 = y[i]['url']
    var2 = x[i]['bodySize']
    sample_dic[var1] = var2


#You want to sort the keys by the values,  maintaining the keys first in a list of tuples, so that the final list will be:
sample_dic = [(k,v) for v,k in sorted(
                 [(v,k) for k,v in sample_dic.items()],reverse=True
                 )
              ]

print(sample_dic)


print("Total Header Size = {}".format(j))
print("Total Body Size = {}".format(k))
print("The Number of Request are Expandable {}".format(Num_request))
print("Number of Expandable Http URLs = " +str(len(ListOfHttpURL)))
print("Number of Expandable Https URLs = " +str(len(ListOfHttpsURL)))
print("Total Transferred Size of Expandable = {}kb (+/- 10kb)".format((j + k)/1000))

server.stop()
# driver.close()
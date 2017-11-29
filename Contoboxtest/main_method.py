from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import json
import os
import pandas as pd
import re
import sys
import operator
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


ad_id =sys.argv[1]

def main():
    server = Server('/Users/harisrizwan/SeleniumEnv/browsermob-proxy-2.1.4/bin/browsermob-proxy')
    server.start()
    proxy = server.create_proxy()
    driverLocation = "/Users/harisrizwan/Selenium/chrome/chromedriver"
    os.environ["chrome.driver"] = driverLocation
    chrome_options = Options()
    chrome_options.add_argument("headless")
    chrome_options.add_argument(f'--proxy-server={proxy.proxy}')
    driver = webdriver.Chrome(driverLocation, chrome_options=chrome_options)
    proxy.new_har()

    driver.get("http://dbb1.contobox.com/v3/preview.php?id=" + str(ad_id))

    # time.sleep(3)
    proxy.wait_for_traffic_to_stop(2000, 6000)

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

    banner_dict= {}

    for i in range(0, pre_http_check):
        w = re.findall(r"\b" + 'https://' + r"\b", d[i]['url'])
        if "https://" in w:
            pre_ListOfHttpsURL.append(d[i]['url'])
        else:
            pre_ListOfHttpURL.append(d[i]['url'])

    m = 0
    n = 0

    for i in range(0, pre_Num_request):
        m = m + v[i]['headersSize']
        n = n + v[i]['bodySize']

    banner_size = (m+n)/1000
    banner_http = len(pre_ListOfHttpURL)
    banner_https = len(pre_ListOfHttpsURL)
    banner_total_request = pre_Num_request


    banner_dict['Pre_Exp weight'] = banner_size
    banner_dict['Pre_Exp # of Http'] = banner_http
    banner_dict['Pre_Exp # of Https'] = banner_https
    banner_dict['Pre_Exp Total Requests'] =banner_total_request

    print(banner_dict)


    # print("Total Header Size = {}".format(m))
    # print("Total Body Size = {}".format(n))
    # print("The Number of Request of Pre-Expandable are {}".format(banner_total_request))
    # print("Number of Pre-Expandable Http URLs = " + str(banner_http))
    # print("Number of Pre-Expandable Https URLs = " + str(banner_https))
    # print("Total Transferred Size of Pre-Expandable = {}kb (+/- 10kb)".format((banner_size) / 1000))

    ################################################################################################


    print("###############***************##############************%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    driver.get("http://dbb1.contobox.com/v3/preview.php?id=" + str(ad_id) + "&tpl=preview_expanded")

    time.sleep(8)



    result = json.dumps(proxy.har)
    json_data = json.loads(result)

    df = pd.DataFrame([x for x in json_data['log']['entries']])

    # df.to_clipboard(index=False)

    y = df['request']
    x = df['response']

    http_check = len(y)
    Num_request = len(x)

    ListOfHttpURL = []
    ListOfHttpsURL = []

    for i in range(0, http_check):
        w = re.findall(r"\b" + 'https://' + r"\b", y[i]['url'])
        if "https://" in w:
            ListOfHttpsURL.append(y[i]['url'])
        else:
            ListOfHttpURL.append(y[i]['url'])

    j = 0
    k = 0
    url_size_dict = {}
    for i in range(0, Num_request):
        j = j + x[i]['headersSize']
        k = k + x[i]['bodySize']
        var1 = y[i]['url']
        var2 = x[i]['bodySize']
        url_size_dict[var1] = var2

    # You want to sort the keys by the values,  maintaining the keys first in a list of tuples, so that the final list will be:
    url_size_dict = [(k, v) for v, k in sorted(
        [(v, k) for k, v in url_size_dict.items()], reverse=True
    )
                  ]

    print(str(len(url_size_dict)))

    expandable_dict = {}

    expandable_size = (j + k) / 1000
    expandable_http = len(ListOfHttpURL)
    expandable_https = len(ListOfHttpsURL)
    expandable_total_request = Num_request

    expandable_dict['Expandable weight'] = expandable_size
    expandable_dict['Expandable # of Http'] = expandable_http
    expandable_dict['Expandable # of Https'] = expandable_https
    expandable_dict['Expandable Total Requests'] = expandable_total_request

    print(expandable_dict)

    # print("Total Header Size = {}".format(j))
    # print("Total Body Size = {}".format(k))
    # print("The Number of Request are Expandable {}".format(Num_request))
    # print("Number of Expandable Http URLs = " + str(len(ListOfHttpURL)))
    # print("Number of Expandable Https URLs = " + str(len(ListOfHttpsURL)))
    # print("Total Transferred Size of Expandable = {}kb (+/- 10kb)".format((j + k) / 1000))

    proxy.clear_dns_cache()

    server.stop()
    driver.quit()

if __name__ == '__main__':
    main()




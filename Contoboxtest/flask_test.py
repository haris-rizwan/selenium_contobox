from flask import Flask, request
import json
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import os
import pandas as pd
import re
import sys
import operator
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def contobox_qa():
    # ad_id = 19250
    ad_id = request.form["ad_id"]
    print(ad_id)
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

    # df.to_clipboard(index=False)

    d = df['request']
    v = df['response']

    pre_http_check = len(d)
    pre_Num_request = len(v)

    pre_ListOfHttpURL = []
    pre_ListOfHttpsURL = []

    preview_data= {}

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

    preview_data['Pre_ExpWeight'] = banner_size
    preview_data['Pre_Exp_#_of_Http'] = banner_http
    preview_data['Pre_Exp_#_of_Https'] = banner_https
    preview_data['Pre_Exp_Total_Requests'] =banner_total_request



    print("###############***************##############************%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    proxy.clear_dns_cache()
    proxy.new_har()

    driver.get("http://dbb1.contobox.com/v3/preview.php?id=" + str(ad_id) + "&tpl=preview_expanded")

    time.sleep(6)



    result = json.dumps(proxy.har)
    json_data = json.loads(result)

    df = pd.DataFrame([x for x in json_data['log']['entries']])

    df.to_clipboard(index=False)

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


    expandable_size = (j + k) / 1000
    expandable_http = len(ListOfHttpURL)
    expandable_https = len(ListOfHttpsURL)
    expandable_total_request = Num_request
    url_size = url_size_dict

    total_size = banner_size + expandable_size
    total_http = banner_http + expandable_http
    total_https = banner_https + expandable_https
    total_requests = banner_total_request + expandable_total_request

    preview_data['ExpandableWeight'] = expandable_size
    preview_data['Expandable_#_of_Http'] = expandable_http
    preview_data['Expandable_#_of_Https'] = expandable_https
    preview_data['ExpandableTotalRequests'] = expandable_total_request
    preview_data['TotalWeightOfContobox'] = total_size
    preview_data['Total_#_of_HTTP_request'] = total_http
    preview_data['Total_#_of_HTTPS_request'] = total_https
    preview_data['Total_#_of_Request_of_Contobox'] = total_requests
    # preview_data['Sorted Url-size list of tuples']= url_size
    # print(type(preview_data))
    # print(preview_data)
    final_preview = json.dumps(preview_data)
    # print(type(final_preview))
    print(final_preview)
    return final_preview

    proxy.clear_dns_cache()

    server.stop()
    driver.quit()


if __name__  == "__main__":
    app.run(debug=True)
from urllib.request import Request, urlopen
from urllib.error import URLError
req = Request("http://dbb1.contobox.com/v3/preview.php?id=12734")
try:
    response = urlopen(req)
    print(response.info())
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    print("it runs")

# from urllib.request import urlopen
# html = urlopen("http://www.google.com/")
# print(html)




from urllib.request import Request, urlopen

req = Request("http://dbb1.contobox.com/v3/preview.php?id=12734")
# url = 'https://www.google.com'
r = urlopen(req)
print(len(r.read()))
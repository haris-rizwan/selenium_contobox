import re



strn = "word hereword word, there word"
search = "word"
print (re.findall(r"\b" + search + r"\b", strn))
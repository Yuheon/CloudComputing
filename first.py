from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.google.com")
bsobject = BeautifulSoup(html,"html.parser")

print(bsobject)

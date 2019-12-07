import requests
from bs4 import BeautifulSoup
import re
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url="https://blog.naver.com/gugu9416/221705114839"
url=url.replace('blog','m.blog');
html = requests.get(url,headers = headers).text

print(url);
soup = BeautifulSoup(html, 'html.parser')

title=str(soup.find_all('p'))

title = re.sub('<.+?>','', title, 0).strip()
title = re.sub(',','',title,0).strip()

search=input()
result1=title.find(search)

search=input()
result2=title.find(search)

a=title[result1:result1+40]
print(a)
a=title[result2:result2+40]
print(a)

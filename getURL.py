import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
search = input()
url += search;
response = requests.get(url)
print(response.encoding)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

urlList = []

for link in soup.find_all('a', {'class': 'url'}):
    url = link.get('href')

    if '://b' not in url:
        if 'blog.me' in url:
            x = re.split('/|:|[.]', url)
            url = 'https://blog.naver.com/' + x[3] + '/' + x[6]
        else:
            continue
    urlList.append(url)
for i in urlList:
    print(i)
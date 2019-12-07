import requests
from bs4 import BeautifulSoup

response = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=청소기')
print(response.encoding)
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')

searchList = []
for search in soup.select(".realtime_srch > ol> li"):
    #searchList.append(search.find('span', {'class':'tit'}).text)
    searchList.append(search.find('span', {'class':'tit'}).text)
for i in range(10):
    print(searchList[i])
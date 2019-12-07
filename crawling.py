import requests
from bs4 import BeautifulSoup
import re

searchurl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
search = input()
keyword1 = input()

searchurl += search+' '+keyword1;
response = requests.get(searchurl)
print(response.encoding)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

urlList = []
count=0
for link in soup.find_all('a', {'class': 'url'}):
    url = link.get('href')

    if '://b' not in url:
        if 'blog.me' in url:
            x = re.split('/|:|[.]', url)
            url = 'https://blog.naver.com/' + x[3] + '/' + x[6]
        else:
            continue
    urlList.append(url)
if len(urlList)==0:
    print('검색 결과 없음')
else :
    for url in urlList:
        
        count=0
        url=url.replace('blog','m.blog');
        response = requests.get(url)
        #print(response.encoding)
        response.encoding = 'utf-8'
        html = response.text
        blog_soup = BeautifulSoup(html, 'html.parser')
        content=blog_soup.find_all('p')
        
        for contents in content:
                if contents.get_text().find(keyword1)>=0:
                    print(contents.get_text())
                    print()
                    count=count+1
        if count>0 :
            print(url)
            print()

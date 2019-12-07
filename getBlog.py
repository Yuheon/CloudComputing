import requests
from bs4 import BeautifulSoup

url = ''  # input url

response = requests.get(url)
# print(response.encoding)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

for j in soup.select('iframe#mainFrame'):
    iframe_url = "http://blog.naver.com" + j.get('src')
    blog_html = requests.get(iframe_url).text

    blog_soup = BeautifulSoup(blog_html, 'html.parser')
    content = blog_soup.find_all('p')

    for contents in content:
        print(contents.get_text())
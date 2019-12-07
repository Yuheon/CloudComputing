from django.shortcuts import render
from .models import Search_list, Result
from django.views import generic
from bs4 import BeautifulSoup
from django.http import HttpResponse
import requests

def main(request):
    template_name = 'cloud/main.html'
    return render(request, template_name)

def check_get(requst):
     template_name = 'cloud/search.html'
     search1 = request.GET.get('search',None)
     keword1 = request.GET.get('',None)
     #db 설정하는거 입력
     firstreview  = FirstReview.object.all()
     secondreview = SecondReview.object.all()
     context = {'firstreview' : firstreview,
             'secondreview' : secondreview}
     firstreview.delete()
     secondreview.delete()
     searchurl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
     searchurl += search1+' '+keyword1;
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
                    firstreview=FirstReview()
                    firstreview.review1=content.get_text()
                    firstreview.review1=url
     
     searchurl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
     searchurl += search2+' '+keyword1;
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
                    secondreview=SecondReview()
                    secondreview.review2=contents.get_text()
                    secondreview.url2=url
           
     return render(request, template_name,context)

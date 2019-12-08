from django.shortcuts import render
from .models import FirstReview, SecondReview
from django.views import generic
from bs4 import BeautifulSoup
from django.http import HttpResponse
import requests
import re

def main(request):
    template_name = 'cloud/main.html'
    return render(request, template_name)

def check_get(request):
     template_name = 'cloud/search.html'
     search1 = request.GET.get('search1',None)
     search2 = request.GET.get('search2',None)
     keyword1 = request.GET.get('keyword',None)
     #db 설정하는거 입력
     firstreview  = FirstReview.objects.all()
     secondreview = SecondReview.objects.all()
     context = {'firstreview' : firstreview,
             'secondreview' : secondreview}
     firstreview.delete()
     secondreview.delete()
     searchurl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
     searchurl += search1+' '+keyword1;
     response = requests.get(searchurl)
     #print(response.encoding)
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
    #if len(urlList)==0:
     #   print('검색 결과 없음')
    #else :
     for url in urlList :
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
                firstreview.review1=contents.get_text()
                firstreview.url1=url
                firstreview.save()
     
     searchurl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
     searchurl += search2+' '+keyword1;
     response = requests.get(searchurl)
     #print(response.encoding)
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
    #if len(urlList)==0:
        #print('검색 결과 없음')
    #else 
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
            secondreview.save()	
           
     return render(request, template_name,context)

from django.shortcuts import render
from .models import Review, SReview, Rank, Shopping
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
     reviews  = Review.objects.all()
     sreviews = SReview.objects.all()
     ranks = Rank.objects.all()
     shoppings = Shopping.objects.all()
     context = {'reviews' : reviews,
             'sreviews' : sreviews,
             'ranks' : ranks,
             'shoppings' : shoppings}
     reviews.delete()
     sreviews.delete()
     ranks.delete()
     shoppings.delete()
     searchurl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
     searchurl += search1+" "+keyword1;
     #searchrank =  'https://search.naver.com/search.naver?where=post&sm=tab_jum&query=' # 검색어 순위를 따로 크롤링 하기위한 url 저장
     #searchrank += search1
     response = requests.get(searchurl)
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
     if len(urlList)==0:
         print('검색 결과 없음')
     else :
         for url in urlList :
             url=url.replace('blog','m.blog')
             response = requests.get(url)
             #print(response.encoding)
             response.encoding = 'utf-8'
             html = response.text
             blog_soup = BeautifulSoup(html, 'html.parser')
             content=blog_soup.find_all('p')
             concatContent=""
             for contents in content:
                 if contents.get_text().find(keyword1)>=0:
                     concatContent+=' '+contents.get_text()
             if concatContent != "":
                 freview = Review()
                 freview.review1=concatContent
                 freview.url=url
                 freview.save()
     searchurl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
     searchurl += search2+" "+keyword1;
     response = requests.get(searchurl)
     #print(response.encoding)
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
     if len(urlList)==0:
         print('검색 결과 없음')
     else :
         for url in urlList :
             url=url.replace('blog','m.blog')
             response = requests.get(url)
             #print(response.encoding)
             print("asdasd")
             response.encoding = 'utf-8'
             html = response.text
             blog_soup = BeautifulSoup(html, 'html.parser')
             content=blog_soup.find_all('p')
             concatContent=""
             for contents in content:
                 if contents.get_text().find(keyword1)>=0:
                     concatContent+=" "+contents.get_text()
             if concatContent!="":
                 sreview=SReview()
                 sreview.review=concatContent
                 sreview.url=url
                 sreview.save()
     searchurl="https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query="
     searchurl+=search1
     response = requests.get(searchurl)
     response.encoding = 'utf-8'
     html = response.text
     soup = BeautifulSoup(html, 'html.parser')
     
     search=soup.find("ol")
     search = str(search.find_all('span',{'class':'tit'}))
     search = re.sub('<.+?>','', search, 0).strip()
     search = re.sub(',','',search,0).strip()
     search = search.replace('[','')
     search.split(' ')
     for i in range(10):
         rank=Rank()
         rank.pname=search.split(' ')[i]
         rank.save()

     url = 'https://search.shopping.naver.com/search/all.nhn?query='
     url += search1;
     response = requests.get(url)
     print(response.encoding)
     response.encoding = 'utf-8'
     html = response.text

     soup = BeautifulSoup(html, 'html.parser')

     imgList = []
     titleList = []
     detailList = []
     priceList = []
     li = soup.find_all('li', {'class': '_itemSection'})
     for i in li:
         shop=Shopping()
         imgLink = i.find('img', {'class': '_productLazyImg'})
         imgList.append(imgLink.get('data-original'))

         title = i.find('a', {'class': 'link'})
         titleList.append(title.get_text())

         prices = i.select_one('span.price > em')
         priceList.append(prices.get_text())

         if i.find('span', {'class': 'detail'}) is not None:
             detail = i.find('span', {'class': 'detail'})
             detailList.append(detail.get_text())
         else:
             detailList.append('')
     for i in range(5):
         shop=Shopping()
         shop.img = imgList[i]
         shop.title = titleList[i]
         shop.detail = detailList[i]
         shop.price = priceList[i]
         shop.save()
     url = 'https://search.shopping.naver.com/search/all.nhn?query='
     url += search2;
     response = requests.get(url)
     print(response.encoding)
     response.encoding = 'utf-8'
     html = response.text

     soup = BeautifulSoup(html, 'html.parser')
     del imgList[:]
     del titleList[:]
     del detailList[:]
     del priceList[:]
    
     li = soup.find_all('li', {'class': '_itemSection'})
     for i in li:
         shop=Shopping()
         imgLink = i.find('img', {'class': '_productLazyImg'})
         imgList.append(imgLink.get('data-original'))

         title = i.find('a', {'class': 'link'})
         titleList.append(title.get_text())

         prices = i.select_one('span.price > em')
         priceList.append(prices.get_text())

         if i.find('span', {'class': 'detail'}) is not None:
             detail = i.find('span', {'class': 'detail'})
             detailList.append(detail.get_text())
         else:
             detailList.append('')
     for i in range(5):
         shop=Shopping()
         shop.img = imgList[i]
         shop.title = titleList[i]
         shop.detail = detailList[i]
         shop.price = priceList[i]
         shop.save()

     return render(request,template_name,context)

     

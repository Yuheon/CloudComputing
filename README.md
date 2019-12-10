# Product Compare
 Product Compare는 실시간 크롤링을 이용한 물품 비교기입니다.  
 물품에대한 리뷰, 스펙, 물품 검색 순위를 보여줌으로 사용자가 쉽게 물품을 비교할수 있습니다.
## Prerequisites
 Product Compare를 이용하기 위해선 다음과 같은 환경을 구성해야합니다.
 * **Linux**   
   
   Linux 가상환경 구현(이 프로젝트에선 AWS를 통하여 가상환경 셋팅)
   Linux webserver는 웹 어플리케이션 구동을 위해 사용
   
 * **Python3**
  
   Python3 는 web crawling 을 위해 사용

 * **Django**  
  
   Python3을 활용한 웹 서버 구현을 위해 요구됨  
    

## Installation   
  ProductCompare 는 python3 환경에서 이용가능합니다.
  
 * python3 환경 구성
     
       $ sudo apt-get install python3 python3-venv
       $ sudo apt-get install python3-pip
       
 * web crawling을 위한 libray 설치
 
       $ pip3 install beautifulsoup4
       $ pip3 install requests

 * django 사용을 위한 설정
    
       $ pip3 install django

 * django 내부 설정
      
       $ sudo apt-get install libssl-dev 
## 사용법 
  django 실행전 인스턴스 port 8000번 개방
  django 실행을 위해선 
       
       cd mysite
       python3 manage.py runserver '자신의 서버 ip':80000
  
  자신의 서버에서 구동하기 위해선
  
      vi mysite/mysite/settings.py
  에서
  
      ALLOWED_HOSTS[
             '자신의 ip 등록'
      ]
  
  ## URL
  http://ec2-35-171-18-79.compute-1.amazonaws.com:8000/#
  
  ## 실행결과
  ![main](https://user-images.githubusercontent.com/43310063/70493292-7bfe1380-1b4a-11ea-8af0-156b9bffc8d6.JPG)
  ![11](https://user-images.githubusercontent.com/43310063/70493349-b7004700-1b4a-11ea-9fe4-414c8fa60c54.JPG)
  ![22](https://user-images.githubusercontent.com/43310063/70493352-b9fb3780-1b4a-11ea-879b-a6720855d023.JPG)
  ![33](https://user-images.githubusercontent.com/43310063/70493355-bb2c6480-1b4a-11ea-9323-499238b956c3.JPG)

 ## merge 오류, history가 겹치지 않은 상태에서 merge를 시도하다가 commit과 branch가 사라졌습니다.
 ![44](https://user-images.githubusercontent.com/43310063/70497415-61319c00-1b56-11ea-826f-84b90711b848.JPG)

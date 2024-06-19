import requests
from bs4 import BeautifulSoup

URL = 'https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&ssc=tab.nx.all&query=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&oquery=%EC%98%81%ED%99%94&tqi=iFZ%2BNdqo1aVssu%2B4ZOhssssstzV-222396&acq=%EC%98%81%ED%99%94&acr=2&qdt=0'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movie = []
        
for item in soup.select('#main_pack ._panel_popular._tab_content ul._panel li'):

    movie.append({
        '순위' : item.select_one('.thumb span.this_text').text,
        '제목' : item.select_one('.title_box strong.name').text,
        '관객 수' : item.select_one('.title_box span.sub_text').text
    })

print(movie)

"""
[{'순위': '1', '제목': '인사이드 아웃 2', '관객 수': '13만명'}, 
{'순위': '2', '제목': '퓨리오사: 매드맥스 사가', '관객 수': '8,101명'}, 
{'순위': '3', '제목': '탈주', '관객 수': '6,959명'}, 
{'순위': '4', '제목': '원더랜드', '관객 수': '6,729명'}, 
{'순위': '5', '제목': '그녀가 죽었다', '관객 수': '5,596명'}, 
{'순위': '6', '제목': '존 오브 인터레스트', '관객 수': '4,407명'}, 
{'순위': '7', '제목': '범죄도시4', '관객 수': '4,234명'}, 
{'순위': '8', '제목': '드라이브', '관객 수': '3,495명'}, 
{'순위': '9', '제목': '몽키맨', '관객 수': '3,079명'}, 
{'순위': '10', '제목': '하이재킹', '관객 수': '2,010명'}, 
{'순위': '11', '제목': '극장판 하이큐!! 쓰레기장의...', '관객 수': '1,296명'}, 
{'순위': '12', '제목': '나쁜 녀 석들: 라이드 오어 ...', '관객 수': '1,260명'}, 
{'순위': '13', '제목': '타로', '관객 수': '1,191명'}, 
{'순위': '14', '제목': '명탐정 코난 VS 괴도 키드', '관객 수': '1,139명'}, 
{'순위': '15', '제목': '키타로 탄생 게게게의 수수께끼', '관객  수': '813명'}, 
{'순위': '16', '제목': '설계자', '관객 수': '682명'}, 
{'순위': '17', '제목': '김준수 콘서트 무비 챕터 원...', '관객 수': '469명'}, 
{'순위': '18', '제목': '기괴도', '관객 수': '379명'}, 
{'순위': '19', '제목': '생츄어리', '관객 수': '273명'}, 
{'순위': '20', '제목': '다우렌의 결혼', '관객 수': '261명'}, 
{'순위': '21', '제목': '너는 달밤에 빛나고', '관객 수': '257명'},
{'순위': '22', '제목': '매드맥스: 분노의 도로', '관객 수': '243명'},
{'순위': '23', '제목': '드림 시나리오', '관객 수': '198명'}, 
{'순위': '24', '제목': '가필드 더 무비', '관객 수': '196명'}, 
{'순위': '25', '제목': '그녀', '관객 수': '188명'}, 
{'순위': '26', '제목': '판문점', '관객 수': '186명'}, 
{'순위': '27', '제목': '쇼처럼 즐거운 인생은 없다', '관객 수': '162명'}, 
{'순위': '28', '제목': '챌린저스', '관객 수': '154명'}, 
{'순위': '29', '제목': '청춘 18X2 너에게로 이어...', '관객 수': '128명'}, 
{'순위': '30', '제목': '창가의 토토', '관객 수': '125명'}]
"""
"""
    코드 작성 단계
    1. requests와 BeautifulSoup 라이브러리 불러오기
    2. URL 정의 및 HTTP GET 요청으로 데이터 가져오기
    3. BeautifulSoup으로 HTML 파싱하기
    4. 데이터 저장을 위한 빈 리스트 초기화
    5. 인기 검색 종목 크롤링 및 리스트에 추가
    6. 주요 해외 지수 크롤링 및 리스트에 추가
    7. 결과 출력
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

popular = []

major = []

for item in soup.select('#popularItemList > li'): # select으로 모든 li를 찾도록 해야 함 # 직계 자식 
    popular.append([item.select_one('a').text, item.select_one('span').text])

print(popular)


for item in soup.select('.lst_major > li'): # li에서 반복이 돌아가야 함
    major.append([item.select_one('a').text, item.select_one('span').text])

print(major)
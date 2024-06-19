"""
    웹 페이지의 테이블 데이터를 파싱하여 딕셔너리 형태로 변환하는 단계
    1. 라이브러리 불러오기
    2. URL 정의 및 데이터 가져오기
    3. HTML 파싱
    4. 테이블 헤더 추출
    5. 테이블 데이터 추출 및 변환
    6. 결과 출력
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

key = []
value = []

for element in soup.find('table').find_all('th'):
    key.append(element.text)

for element in soup.find('table').find('tbody').find_all('tr'):
    temp = []
    for td_element in element.find_all('td'):
        temp.append(td_element.text)
    value.append(dict(zip(key, temp)))

print(value)
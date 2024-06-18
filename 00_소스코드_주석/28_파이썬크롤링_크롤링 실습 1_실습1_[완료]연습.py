"""
    웹 크롤링의 기본적인 단계
    1. 라이브러리 불러오기
    2. URL 정의 및 데이터 가져오기
    3. HTML 파싱
    4. 필요한 데이터 추출
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

element = soup.select_one('#cook')
print(element.text)
""" 
    문제.
    사이트내에 인기검색종목과 주요해외지수를 각각 상한가인 종목만 크롤링하여 
    종목명과 주가지수를 아래와같이 리스트로 정리해주세요
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

popular = []

major = []

for item in soup.select('#popularItemList > .up'): # list내의 항목을 순회하며 데이터를 추출하기 위해 for문을 사용
    popular.append([item.select_one('a').text, item.select_one('span').text])

print(popular)

for item in soup.select('.lst_major > .up'):
    major.append([item.select_one('a').text, item.select_one('span').text])

print(major)

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

for item in soup.select("#popularItemList li"):
    # 각 'li' 요소 내의 'img' 태그의 'alt' 속성값이 '상한'인지 확인함.
    if item.select_one('img').attrs['alt'] == '상한':
        # '상한'인 경우 'a' 태그의 텍스트와 'span' 태그의 텍스트를 추출하여 'popular' 리스트에 추가함.
        popular.append([item.select_one('a').text, item.select_one('span').text])

for item in soup.select(".lst_major li"):
    # 각 'li' 요소 내의 'img' 태그의 'alt' 속성값이 '상한'인지 확인함.
    if item.select_one('img').attrs['alt'] == '상한':
        # '상한'인 경우 'a' 태그의 텍스트와 'span' 태그의 텍스트를 추출하여 'major' 리스트에 추가함.
        major.append([item.select_one('a').text, item.select_one('span').text])

print(popular)

print(major)

"""
    결과.
    [['써니전자', '5,000'], ['안랩', '81,000'], ['케이엠더블..', '57,300'], ['피피아이', '12,600'], ['삼성전자우', '45,600'], ['SK하이닉스', '94,700']]

    [['다우산업', '28,647.43'], ['나스닥', '9,015.03'], ['홍콩H', '11,320.56'], ['상해종합', '3,085.20']]
"""

"""
    문제.
    사이트내에 인기검색종목과 주요해외지수를 각각 크롤링하여 
    종목명과 상한, 하한여부를 아래와같이 리스트로 정리해주세요
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

# 'popular' 아이템 리스트를 저장할 리스트 초기화.
popular = []

# 'major' 아이템 리스트를 저장할 리스트 초기화.
major = []

# '#popularItemList li' 선택자를 사용하여 모든 'li' 요소를 찾음.
for item in soup.select("#popularItemList li"):
    # 각 'li' 요소 내의 'a' 태그의 텍스트와 'img' 태그의 'alt' 속성값을 추출하여 리스트에 추가함.
    popular.append([item.select_one("a").text, item.select_one("img").attrs['alt']])

# 'popular' 리스트의 내용을 출력함.
print(popular)

# 'ul.lst_major li' 선택자를 사용하여 모든 'li' 요소를 찾음.
for item in soup.select("ul.lst_major li"):
    # 각 'li' 요소 내의 'a' 태그의 텍스트와 'img' 태그의 'alt' 속성값을 추출하여 리스트에 추가함.
    major.append([item.select_one("a").text, item.select_one("img").attrs['alt']])

# 'major' 리스트의 내용을 출력함.
print(major)


"""
    결과.
    [['써니전자', '상한'], ['삼성전자', '하락'], ['안랩', '상승'], ['케이엠더블..', '상승'], ['피피아이', '상한'], ['KT&G', '하락'], ['삼성전자우', '상승'], ['대양금속', '하한'], ['SK하이닉스', '상승'], ['SK텔레콤', '하락']]
    [['다우산업', '상한'], ['나스닥', '상한'], ['홍콩H', '상한'], ['상해종합', '상한'], ['니케이225', '하락']]
"""
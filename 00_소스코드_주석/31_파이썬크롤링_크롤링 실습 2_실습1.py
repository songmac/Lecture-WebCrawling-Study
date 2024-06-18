"""
    문제.
    사이트내에 인기검색종목과 주요해외지수를 각각 크롤링하여 
    종목명과 주가지수를 아래와같이 리스트로 정리해주세요.
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

# '#popularItemList > li' 선택자를 사용하여 모든 'li' 요소를 찾음.
for item in soup.select('#popularItemList > li'):
    # 각 'li' 요소 내의 'a' 태그와 'span' 태그의 텍스트를 추출하여 리스트에 추가함.
    popular.append([item.select_one('a').text, item.select_one('span').text])
    
# 'popular' 리스트의 내용을 출력함.
print(popular)

# '.lst_major > li' 선택자를 사용하여 모든 'li' 요소를 찾음.
for item in soup.select('.lst_major > li'):
    # 각 'li' 요소 내의 'a' 태그와 'span' 태그의 텍스트를 추출하여 리스트에 추가함.
    major.append([item.select_one('a').text, item.select_one('span').text])
    
# 'major' 리스트의 내용을 출력함.
print(major)


"""
    결과.
    [['써니전자', '5,000'], ['삼성전자', '55,200'], ['안랩', '81,000'], ['케이엠더블..', '57,300'], ['피피아이', '12,600'], ['KT&G', '92,500'], ['삼성전자우', '45,600'], ['대양금속', '10,550'], ['SK하이닉스', '94,700'], ['SK텔레콤', '234,000']]

    [['다우산업', '28,647.43'], ['나스닥', '9,015.03'], ['홍콩H', '11,320.56'], ['상해종합', '3,085.20'], ['니케이225', '23,656.62']]
"""
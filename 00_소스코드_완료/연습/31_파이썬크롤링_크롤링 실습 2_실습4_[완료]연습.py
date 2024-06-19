"""
    문제.
    분양중인 아파트 정보를 크롤링하여 아래와 같이 딕셔너리 형태로 정리해주세요
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

apt = []

for item in soup.select('.sale_list li'):
    apt.append({
        '이름': item.select_one('.sale_tit').text.strip(),
        '분양가' : item.select('.detail_info dd.txt')[0].select_one('strong').text.replace(',',''),
        '유형' : item.select('.detail_info dd.txt')[1].text.split('|')[0], 
        '분양유형' : item.select('.detail_info dd.txt')[1].text.split('|')[1],
        '세대수' : item.select('.detail_info dd.txt')[2].text.split('|')[0],        
        '평형' : item.select('.detail_info dd.txt')[2].text.split('|')[1]
    })

# print(apt)

for a in apt:
    print(a) # 딕셔너리를 한 줄씩 출력

"""
결과.
[{'이름': 'H하우스장위',  '분양가': '16000',  '유형': '아파트',  '분양유형': '일반민간임대',  '세대수': '분양 134세대',  '평형': '45㎡~65㎡'},
 {'이름': '고덕리엔파크2단지 장기전세',  '분양가': '38400',  '유형': '아파트',  '분양유형': '장기전세주택',  '세대수': '분양 1세대',  '평형': '149㎡'},
 {'이름': '신정이펜하우스3단지 장기전세',  '분양가': '39040',  '유형': '아파트',  '분양유형': '장기전세주택',  '세대수': '분양 1세대',  '평형': '148㎡'},
 {'이름': '천왕이펜하우스2단지 장기전세',  '분양가': '38240',  '유형': '아파트',  '분양유형': '장기전세주택',  '세대수': '분양 1세대',  '평형': '142㎡'},
 {'이름': '송파파크데일2단지 장기전세',  '분양가': '45600',  '유형': '아파트',  '분양유형': '장기전세주택',  '세대수': '분양 1세대',  '평형': '150㎡'}]
"""
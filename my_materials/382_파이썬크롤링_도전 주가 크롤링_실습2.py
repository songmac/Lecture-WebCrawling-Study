"""
    문제. 
    전일대비 상승한 항목만 종목명, 현재가, 전일비를 크롤링해주세요.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/sise_quant.nhn'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

stock_list = []

for tr_item in soup.select('#contentarea .box_type_l > table > tr')[2:]:
    if tr_item.select_one('td[colspan]'):
        continue
    
    if tr_item.select_one('span.blind').text == '상승':

        stock_item = []
        for td_item in tr_item.select('td')[0:4]:
            stock_item.append(td_item.text.strip().replace('상승','').replace('\n','').replace('\t', ''))
            
        # 추출한 데이터를 문자열로 결합하여 stock_list에 추가함.
        stock_list.append(' '.join(stock_item))

# 추출된 주식 정보를 한 줄씩 출력함.
for stock in stock_list:
    print(stock)


"""
    결과.
    7 한화시스템 21,700 2,150
    8 KIB플러그에너지 615 52
    9 삼성전자 79,800 1,700
    11 한국가스공사 55,800 2,500
    12 한국석유 19,860 2,200
    13 KODEX 레버리지 20,145 380
    14 KC코트렐 1,214 176
    15 한전산업 13,270 1,370
    17 SG글로벌 2,330 135
    19 이수페타시스 56,100 3,700
    20 동양생명 6,500 1,260
    22 화승알앤에이 5,100 200
    23 CJ씨푸드 6,080 40
    24 사조씨푸드 6,940 360
    25 삼영 3,945 295
    26 KEC 1,404 11
    28 두산에너빌리티 19,720 40
    29 한화생명 2,865 105
    30 플레이그램 1,193 128
    33 한국패러랠 244 5
    34 사조동아원 1,173 1
    35 TIGER 화장품 3,550 50
    36 한온시스템 5,020 250
    39 대한전선 15,790 140
    43 KODEX 코스닥150 13,815 10
    44 동방 2,975 10
    47 코오롱글로벌 12,110 830
    48 SK하이닉스 234,500 11,500
    49 TIGER 미국필라델피아반도체나스닥 20,925 360
    50 신송홀딩스 9,610 310
    51 HMM 17,930 390
    53 비에이치 25,000 1,650
    54 KODEX 200 37,845 395
    55 TIGER 미국테크TOP10 INDXX 21,405 245
    59 기아 131,000 1,900
    61 대한제당 3,455 65
    62 대성에너지 9,770 150
    63 샘표식품 40,350 5,550
    64 KG케미칼 5,280 220
    65 금호건설 3,980 270
    68 TIGER 미국S&P500 18,870 160
    69 TIGER Fn반도체TOP10 14,320 280
    70 KODEX 자동차 22,285 195
    72 디아이 21,800 1,150
    74 대상홀딩스 12,820 340
    76 KODEX 미국AI테크TOP10+15%프리미엄 10,995 95
    78 DB하이텍 45,400 1,750
    79 토니모리 15,080 700
    80 그린케미칼 8,310 450
    84 현대차 283,000 4,500
    85 삼성전자우 62,900 500
    86 한국전력 19,840 100
    91 SK네트웍스 5,000 95
    92 백광산업 14,680 120
    97 신성이엔지 2,060 40
    100 KODEX AI반도체핵심장비 14,610 110
"""
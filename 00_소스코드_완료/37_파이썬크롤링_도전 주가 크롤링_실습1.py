"""
    문제. 
    종목명과 현재가를 크롤링해주세요.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://finance.naver.com/sise/sise_quant.nhn'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

stock_list = []

# tr(테이블 행) 요소를 순회하며 데이터를 추출함.
# 여기서 [2:]는 테이블 헤더 등을 건너뛰고 실제 데이터 행부터 순회하기 위한 것임.
for tr_item in soup.select('#contentarea .box_type_l > table > tr')[2:]:
    # tr 요소 내에 td[colspan] 속성을 가진 요소가 있는 경우 해당 tr 요소를 무시함.
    # td[colspan]은 css셀렉터에서 속성 태그를 선택하는 방법임.
    if tr_item.select_one('td[colspan]'):
        continue
    
    # 각 행(tr)에서 추출한 데이터를 임시로 저장할 리스트를 초기화함.
    stock_item = []
    
    # tr 요소 내의 td(테이블 데이터 셀) 요소 중 첫 3개 요소를 순회하며 텍스트를 추출함.
    for td_item in tr_item.select('td')[:3]:
        # 텍스트의 앞뒤 공백을 제거하고 리스트에 추가함.
        stock_item.append(td_item.text.strip())
    
    # 추출한 데이터를 문자열로 결합하여 stock_list에 추가함.
    stock_list.append(' '.join(stock_item))

# 추출된 주식 정보를 한 줄씩 출력함.
for stock in stock_list:
    print(stock)


"""
    결과.
    1 KODEX 200선물인버스2X 1,958
    2 삼성 인버스 2X WTI원유 선물 ETN 92
    3 한국ANKOR유전 481
    4 동양철관 1,090
    5 KODEX 코스닥150선물인버스 3,520
    6 KODEX 인버스 4,090
    7 한화시스템 21,700
    8 KIB플러그에너지 615
    9 삼성전자 79,800
    10 KODEX 코스닥150레버리지 10,945
    11 한국가스공사 55,800
    12 한국석유 19,860
    13 KODEX 레버리지 20,145
    14 KC코트렐 1,214
    15 한전산업 13,270
    16 삼성공조 15,740
    17 SG글로벌 2,330
    18 신한 인버스 2X WTI원유 선물 ETN(H) 79
    19 이수페타시스 56,100
    20 동양생명 6,500
    21 국제약품 5,760
    22 화승알앤에이 5,100
    23 CJ씨푸드 6,080
    24 사조씨푸드 6,940
    25 삼영 3,945
    26 KEC 1,404
    27 대원전선 3,545
    28 두산에너빌리티 19,720
    29 한화생명 2,865
    30 플레이그램 1,193
    31 포스코인터내셔널 66,600
    32 현대로템 40,200
    33 한국패러랠 244
    34 사조동아원 1,173
    35 TIGER 화장품 3,550
    36 한온시스템 5,020
    37 서울식품 190
    38 TIGER 2차전지TOP10 11,300
    39 대한전선 15,790
    40 화신 14,100
    41 마니커 1,262
    42 에이프로젠 1,304
    43 KODEX 코스닥150 13,815
    44 동방 2,975
    45 TIGER 차이나전기차SOLACTIVE 7,785
    46 삼성 인버스 2X 코스닥150 선물 ETN 6,195
    47 코오롱글로벌 12,110
    48 SK하이닉스 234,500
    49 TIGER 미국필라델피아반도체나스닥 20,925
    50 신송홀딩스 9,610
    51 HMM 17,930
    52 삼성중공업 8,860
    53 비에이치 25,000
    54 KODEX 200 37,845
    55 TIGER 미국테크TOP10 INDXX 21,405
    56 대한해운 2,240
    57 보해양조 510
    58 KODEX 미국30년국채액티브(H) 9,895
    59 기아 131,000
    60 KODEX 2차전지산업레버리지 3,265
    61 대한제당 3,455
    62 대성에너지 9,770
    63 샘표식품 40,350
    64 KG케미칼 5,280
    63 샘표식품 40,350
    64 KG케미칼 5,280
    65 금호건설 3,980
    66 다이나믹디자인 4,970
    67 TIGER 2차전지TOP10레버리지 2,820
    68 TIGER 미국S&P500 18,870
    69 TIGER Fn반도체TOP10 14,320
    70 KODEX 자동차 22,285
    71 넥스틸 8,700
    72 디아이 21,800
    73 LG디스플레이 10,120
    74 대상홀딩스 12,820
    75 삼부토건 1,573
    76 KODEX 미국AI테크TOP10+15%프리미엄 10,995
    77 TIGER 200선물인버스2X 2,090
    78 DB하이텍 45,400
    79 토니모리 15,080
    80 그린케미칼 8,310
    81 한화솔루션 29,650
    82 삼성E&A 21,950
    83 팬오션 4,000
    84 현대차 283,000
    85 삼성전자우 62,900
    86 한국전력 19,840
    87 화승코퍼레이션 2,035
    88 흥아해운 2,335
    89 한투 인버스 2X 나스닥 100 ETN 811
    90 TIGER 2차전지소재Fn 6,795
    91 SK네트웍스 5,000
    92 백광산업 14,680
    93 에코프로머티 102,700
    94 아센디오 1,225
    95 맥쿼리인프라 12,600
    96 KR모터스 694
    97 신성이엔지 2,060
    98 TIGER 인도빌리언컨슈머 11,010
    99 KODEX 미국30년국채+12%프리미엄(합성 H) 10,480
    100 KODEX AI반도체핵심장비 14,610
"""
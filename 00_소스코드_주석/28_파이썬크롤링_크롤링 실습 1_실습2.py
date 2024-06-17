"""
    문제.
    HTML 문서내에 TABLE 내에 th 와 td에 있는 값들을 크롤링해 아래와 같은 딕셔너리 형태를 만들어보세요.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# 테이블의 헤더를 저장할 리스트 초기화.
key = []
# 테이블의 값을 저장할 리스트 초기화.
value = []

# 테이블에서 모든 'th' 요소를 찾아 key 리스트에 추가함.
for element in soup.find('table').find_all('th'):
    key.append(element.text)
# print(key) # ['이름', '나이']

# 테이블의 본문('tbody')에서 모든 'tr' 요소를 찾아 각 행의 데이터를 추출함.
for element in soup.find('table').find('tbody').find_all('tr'):
    # 각 행의 데이터를 임시로 저장할 리스트 초기화.
    temp = []
    # 현재 행에서 모든 'td' 요소를 찾아 temp 리스트에 추가함.
    for td_element in element.find_all('td'):
        temp.append(td_element.text)
    # print(temp) # 첫번째 tr에서 ['이몽룡', '34'] # 두번째 tr에서 ['홍길동', '23']

    # key 리스트와 temp 리스트를 딕셔너리로 묶어서 value 리스트에 추가함.
    value.append(dict(zip(key, temp)))
"""
    zip?
    여러 개의 iterable (예: 리스트, 튜플 등)을 병렬로 순회.

    예제.
    # 두 개의 리스트가 있다고 가정.
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]
    # zip 함수를 사용하여 두 리스트를 병렬로 순회하며, 각 요소를 튜플로 묶어줌.
    zipped = zip(list1, list2)
    # zip 함수의 결과를 리스트로 변환하여 출력.
    print(list(zipped))
"""

# 추출된 값을 출력함.
print(value)

"""
    결과.
    [{'이름': '이몽룡', '나이': '34'}, {'이름': '홍길동', '나이': '23'}]
"""
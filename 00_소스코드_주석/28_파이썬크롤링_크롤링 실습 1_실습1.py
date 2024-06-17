"""
    문제.
    HTML 문서내에 ID가 cook 인 태그내의 내용을 출력해주세요.
"""


# requests와 BeautifulSoup 라이브러리를 불러옴.
import requests
from bs4 import BeautifulSoup 

# 크롤링하려는 웹 페이지의 URL을 정의함.
URL = 'https://crawlingstudy-dd3c9.web.app/01/'

"""
    객체란?
    객체는 데이터(속성)와 그 데이터와 관련된 동작(메서드)을 포함하는 독립적인 단위. 
    객체는 특정 클래스의 인스턴스(instance).

    response는 requests.models.Response 클래스의 인스턴스이고, 
    soup은 bs4.BeautifulSoup 클래스의 인스턴스.
"""
# requests.get을 사용하여 해당 URL의 웹 페이지 내용을 가져옴.
response = requests.get(URL)
# print(response) # <Response [200]>
print('----------------------------------------------------------')

# response.text를 사용하여 응답의 내용을 텍스트 형태로 가져옴.
# BeautifulSoup을 사용하여 HTML 콘텐츠를 파싱함.
"""
    파싱(Parsing)?
    HTML 문서를 읽어 들여서 특정 규칙에 따라 데이터를 분해하고 구조화하는 과정.
    HTML 문서의 텍스트를 분석하여 컴퓨터가 이해할 수 있는 (계층/트리)구조로 변환.
"""
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)
print('----------------------------------------------------------')

# 선택자를 사용하여 특정 HTML 요소를 찾음.
# 여기서는 ID가 'cook'인 요소를 선택함.
element = soup.select_one("#cook")
# print(element)

# 선택된 요소의 텍스트 내용을 출력함.
print(element.text)



"""
    결과.
    전통적인 요리법이나 양식은 상당한 차이가 있지만, 이탈리아 요리는 다른 국가의 요리 문화에서 다양한 
    영 감을 줄 만큼 다양하고 혁신적인 것으로 평가되고 있다. 각 지방마다 고유의 특색이 있어 그 양식도 
    다양하지만 크게 북부와 남부로 나눌 수 있다. 다른 나라와 국경을 맞대고 있던 북부 지방은 산업화되어 
    경제적으로 풍족하 고 농업이 발달해 쌀이 풍부해 유제품이 다양한 반면 경제적으로 침체되었던 남부 지방은 
    올리브와 토마토, 모차렐라 치즈가 유명하고 특별히 해산물을 활용한 요리가 많다. 식재료와 치즈 등의 차이는 
    파스타의 종류와 소스와 수프 등도 다름을 의미한다.
"""
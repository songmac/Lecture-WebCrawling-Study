"""
    문제. 
    HTML 문서내에 모든 A 태그에 링크된 페이지에 있는 내용을 읽어 출력해주세요.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# 웹 페이지 내의 모든 'a' 태그(링크)를 찾음.
for atag in soup.find_all('a'):
    # 각 'a' 태그의 'href' 속성값을 사용하여 새로운 URL을 만듦.
    new_url = 'https://crawlingstudy-dd3c9.web.app/01/' + atag.attrs['href']
    
    # 새로운 URL로 HTTP GET 요청을 보냄.
    response = requests.get(new_url)
    
    # 새로운 페이지의 HTML 콘텐츠를 파싱함.
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 새로운 페이지에서 첫 번째 'p' 태그의 텍스트 내용을 가져와서 양쪽 공백을 제거한 후 출력함.
    print(soup.find('p').text.strip())

"""
    결과. 
    크롤링 연습사이트 01-1 페이지입니다.
    크롤링 연습사이트 01-2 페이지입니다.
    크롤링 연습사이트 01-3 페이지입니다.
    크롤링 연습사이트 01-4 페이지입니다.
"""
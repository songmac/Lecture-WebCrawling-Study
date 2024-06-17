from bs4 import BeautifulSoup
import requests

# 웹 페이지 가져오기
url = 'https://crawlingstudy-dd3c9.web.app/01/'


response = requests.get(url)
html = response.text

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 원하는 요소 선택하기
title = soup.title  # 웹 페이지의 타이틀 태그
paragraph = soup.find('p')  # 첫 번째 <p> 태그

# 텍스트 추출
print(title.text)
print(paragraph.text)

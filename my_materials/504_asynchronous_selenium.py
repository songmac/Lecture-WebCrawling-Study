from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Selenium 웹드라이버 설정
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 웹사이트 열기
driver.get('https://jsonplaceholder.typicode.com/posts')

# 페이지가 완전히 로드될 때까지 대기 (필요에 따라 조정)
time.sleep(5)

# 페이지 소스 가져오기
html = driver.page_source

# BeautifulSoup으로 파싱
soup = BeautifulSoup(html, 'html.parser')

# 원하는 데이터 찾기 (예: div#post)
post_content = soup.find('div', {'id': 'post'})

# 결과 출력
print(post_content)

# 브라우저 닫기
driver.quit()


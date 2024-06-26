import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

# 엑셀 파일 생성
wb = Workbook(write_only=True)
ws = wb.create_sheet('코스타그램')
ws.append(['이미지주소', '내용', '해시태그', '좋아요 수', '댓글 수'])

# 웹 드라이버 설정
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 브라우저 줌 레벨 설정
driver.get('chrome://settings/')
driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.50);')
time.sleep(1)

# 웹 페이지 접속 
driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(1)

# 로그인
driver.find_element(By.CSS_SELECTOR, '.top-nav__login-link').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.login-container__login-input').send_keys('codeit')
driver.find_element(By.CSS_SELECTOR, '.login-container__password-input').send_keys('datascience')

driver.find_element(By.CSS_SELECTOR, '.login-container__login-button').click()
time.sleep(2)

# 페이지 끝까지 스크롤
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 모든 썸네일 요소 가져오기
posts = driver.find_elements(By.CSS_SELECTOR, '.post-list__post')

for post in posts:
    # 썸네일 클릭
    post.click()
    time.sleep(0.5)

    # 이미지 주소 가져오기
    style_attr = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.post-container__image'))
    ).get_attribute('style')
    image_url = style_attr.split('"')[1]

    # 내용, 해시태그, 좋아요 수, 댓글 수 가져오기
    content = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.content__text'))
    ).text
    hashtag = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'span.content__tag'))
    )
    hashtags = ' '.join([tag.text for tag in hashtag])  # 해시태그를 하나의 문자열로 결합
    like_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.content__like-count'))
    ).text
    comment_count = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.content__comment-count'))
    ).text

    ws.append([image_url, content, hashtags, like_count, comment_count])

    # 닫기 버튼 클릭
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.close-btn'))
    )
    close_button.click()
    time.sleep(0.5)

driver.quit()

# 엑셀 파일 저장
wb.save('코스타그램.xlsx')

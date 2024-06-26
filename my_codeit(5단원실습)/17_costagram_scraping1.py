from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.top-nav__login-link').click()
time.sleep(1)

# 코스타그램 로그인
id_box = driver.find_element(By.CSS_SELECTOR, '.login-container__login-input') # 요소가 class라는 것을 유의
pw_box = driver.find_element(By.CSS_SELECTOR, '.login-container__password-input')
login_button = driver.find_element(By.CSS_SELECTOR, '.login-container__login-button')

(ActionChains(driver)
    .send_keys_to_element(id_box, 'codeit')
    .send_keys_to_element(pw_box, 'datascience')
    .click(login_button)
    .perform()
 )
time.sleep(1)

# 웹페이지 끝까지 스크롤
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 대소문자 주의

    time.sleep(0.5)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 각 썸네일(포스팅)을 클릭하고, 창이 뜨면 닫기 버튼 누르기
posts = driver.find_elements(By.CSS_SELECTOR, '.post-list__post')

image_urls = []
for post in posts:
    # 썸네일 클릭
    post.click()
    time.sleep(0.5)

    # 닫기 버튼 누르기
    driver.find_element(By.CSS_SELECTOR, '.close-btn').click()
    time.sleep(0.5)


# 웹 드라이버 종료
driver.quit()
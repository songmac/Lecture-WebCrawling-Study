from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 드라이버 설정
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 브라우저 줌 레벨 설정
driver.get('chrome://settings/')
driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.50);')
time.sleep(1)

driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(1)

# 로그인 링크 클릭
login_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-nav__login-link'))
)
login_link.click()
time.sleep(1)

# 코스타그램 로그인
id_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__login-input'))
)
pw_box = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__password-input'))
)
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.login-container__login-button'))
)

ActionChains(driver).send_keys_to_element(id_box, 'codeit').perform()
ActionChains(driver).send_keys_to_element(pw_box, 'datascience').perform()
ActionChains(driver).click(login_button).perform()
time.sleep(2)

# 웹페이지 끝까지 스크롤
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # 새로운 포스트가 로드될 때까지 대기
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.post-list__post:nth-child(' + str(len(driver.find_elements(By.CSS_SELECTOR, '.post-list__post')) + 1) + ')'))
            )
        except:
            break
    last_height = new_height
    time.sleep(1)

# 각 썸네일(포스팅)을 클릭하고, 창이 뜨면 닫기 버튼 누르기
posts = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.post-list__post'))
)

image_urls = []
for post in posts:
    # 썸네일 클릭
    post.click()
    time.sleep(0.5)

    # 이미지 URL 가져오기
    image_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.post-container__image'))
    )
    style_attr = image_element.get_attribute('style')
    image_path = style_attr.split('"')[1]
    image_url = "https://workey.codeit.kr" + image_path
    image_urls.append(image_url)

    # 닫기 버튼 누르기
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.close-btn'))
    )
    close_button.click()
    time.sleep(0.5)

print(image_urls)

# 웹 드라이버 종료
driver.quit()

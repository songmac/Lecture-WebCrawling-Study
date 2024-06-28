# 안정적으로 크롤링 할 수 있도록 대기 시간 발생

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver 서비스 설정 (webdriver-manager를 사용하여 자동으로 설치 및 설정)
service = Service(ChromeDriverManager().install())

# 옵션 객체 생성
options = Options()
# 'detach' 옵션을 True 로 설정하여 스크립트 실행이 끝난 후에도 브라우저가 열려있게 만듬
options.add_experimental_option("detach", True)
# 로그 레벨을 낮추기 위한 옵션 추가
# options.add_argument("--log-level=3")  # INFO 이하 로그만 출력

# ChromeDriver 실행 (옵션 전달)
driver = webdriver.Chrome(service=service, options=options)

# 암묵적 대기 설정
driver.implicitly_wait(3)

# 웹페이지 열기
driver.get('https://workey.codeit.kr/costagram/index')

# 로그인 버튼 클릭 (명시적 대기 사용)
login_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-nav__login-link'))
)
login_link.click()

# 사용자명 입력
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.login-container__login-input'))
)
username_input.send_keys('codeit')

# 비밀번호 입력
password_input = driver.find_element(By.CSS_SELECTOR, '.login-container__password-input')
password_input.send_keys('datascience')

# 로그인 버튼 클릭
login_button = driver.find_element(By.CSS_SELECTOR, '.login-container__login-button')
login_button.click()

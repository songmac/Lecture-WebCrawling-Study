# selenium 4.0 이상에서 사용하는 코드
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/costagram/index')
driver.find_element(By.CSS_SELECTOR, '.top-nav__login-link').click()

driver.find_element(By.CSS_SELECTOR, '.login-container__login-input').send_keys('codeit')
driver.find_element(By.CSS_SELECTOR, '.login-container__password-input').send_keys('datascience')

driver.find_element(By.CSS_SELECTOR, '.login-container__login-button').click()

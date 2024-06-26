from selenium import webdriver
from selenium.webdriver.common.by import By

# 웹 드라이버 설정
driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/orangebottle/index')

branch_infos = []

# 모든 지점에 대한 웹 요소 가져오기
branches = driver.find_elements(By.CSS_SELECTOR, 'div.branch')

for branch in branches:
    # 각 branch 요소에서 지점 이름, 전화번호 가져오기
    branch_name = branch.find_element(By.CSS_SELECTOR, 'p.city').text
    address = branch.find_element(By.CSS_SELECTOR, 'p.address').text
    phone_number = branch.find_element(By.CSS_SELECTOR, 'span.phoneNum').text
    branch_infos.append([branch_name, address, phone_number])

driver.quit()

# 테스트 코드
print(branch_infos)
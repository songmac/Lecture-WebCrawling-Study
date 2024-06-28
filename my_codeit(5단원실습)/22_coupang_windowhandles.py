import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

# 쿠팡 '커피' 검색 결과 페이지 접속
driver.get('https://www.coupang.com/np/search?component=&q=%EC%BB%A4%ED%94%BC&channel=user')
time.sleep(2)

# 모든 제품 링크 찾기
products = driver.find_elements(By.CSS_SELECTOR, 'li.search-product a.search-product-link')

# 검색 결과 창 핸들을 저장
search_result_window = driver.current_window_handle

for index, product in enumerate(products):
    try:
        # 제품 링크 클릭
        product.click()
        
        # 새 창이 열릴 때까지 대기
        WebDriverWait(driver, 10).until(EC.new_window_is_opened(driver.window_handles))
        
        # 새 창의 핸들을 가져와서 전환
        new_window = [window for window in driver.window_handles if window != search_result_window][0]
        driver.switch_to.window(new_window)
        
        # 디버깅 메시지: 새 창의 제목 출력
        print(f"New window title: {driver.title}")
        
        # 선택 사항: 새 창에서 데이터 스크래핑 등 작업 수행
        
        # 새 창 닫기
        driver.close()
        
        # 검색 결과 창으로 다시 전환
        driver.switch_to.window(search_result_window)
    
    except Exception as e:
        print(f"Error processing product {index}: {e}")
        # 오류가 발생해도 계속 진행하기 위해 검색 결과 창으로 다시 전환
        driver.switch_to.window(search_result_window)

driver.quit()

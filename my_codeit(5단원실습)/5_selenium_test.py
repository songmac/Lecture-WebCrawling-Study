# Selenium 임포트
from selenium import webdriver
# Selenium의 Chrome 옵션을 설정하기 위한 Options 클래스를 가져옴
from selenium.webdriver.chrome.options import Options


# 옵션 객체 생성
options = Options()
# 'detach' 옵션을 True 로 설정하여 스크립트 실행이 끝난 후에도 브라우저가 열려있게 만듬
options.add_experimental_option("detach", True)

# 설정한 옵션을 적용
driver = webdriver.Chrome(options=options)    

# 사이트 접속하기
driver.get('https://codeit.kr')

# # 크롬 드라이버 종료
# driver.quit() 







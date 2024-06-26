import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from openpyxl import Workbook

# 워크북 생성
wb = Workbook(write_only=True)
ws = wb.create_sheet()
ws.append(['선수명', '타율', '게임수', '타수', '득점', '안타', '홈런'])

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

# 웹사이트 접속
url = 'https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx'
driver.get(url)
time.sleep(1)

# 년도 선택
year_select = Select(driver.find_element(By.CSS_SELECTOR, '#cphContents_cphContents_cphContents_ddlSeason_ddlSeason'))
year_select.select_by_visible_text('2023')
time.sleep(1)

# 팀선택
team_select = Select(driver.find_element(By.CSS_SELECTOR, '#cphContents_cphContents_cphContents_ddlTeam_ddlTeam'))
team_select.select_by_visible_text('한화')
time.sleep(1)

# 필요한 정보 가져오기
results = driver.find_elements(By.CSS_SELECTOR, '.record_result tbody tr')

for trs in results:
    tds = trs.find_elements(By.TAG_NAME, 'td')
    # 순서(0 ~ 15): 순위, 선수명, 팀명, AVG, G, PA, AB, R, H, 2B, 3B, HR, TB, RBI, SAC, SF 
    player = tds[1].text
    avg = tds[3].text
    game = tds[4].text
    at_bats = tds[6].text
    runs = tds[7].text
    hits = tds[8].text
    home_run = tds[11].text

    ws.append([player, avg, game, at_bats, runs, hits, home_run])


wb.save('한화_2023년_타자기록.xlsx')
# 웹 드라이버 종료 필요시
driver.quit()
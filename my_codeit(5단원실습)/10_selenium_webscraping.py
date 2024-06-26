import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/music')
time.sleep(1)

popular_artists = []
for artist in driver.find_elements(By.CSS_SELECTOR, 'ul.popular__order li'):
    popular_artists.append(artist.text.strip())

print(popular_artists)
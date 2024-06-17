from selenium import webdriver
import time

chromedriver = 'c:/webdriver/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get("https://www.jungle.co.kr/")
button = driver.find_element_by_css_selector("div#existMore a#more")

cursor = 0
datas = []

for i in range(10):
    button.click()
    time.sleep(2)
    items = driver.find_elements_by_css_selector("ul.thumb_list > li")
    cnt = len(items)
    
    for idx in range(cursor, cnt):
        datas.append({
            'title': items[idx].find_element_by_css_selector("span.title").text,
            'category': items[idx].find_element_by_css_selector("a.thumb_cate").text
        })
    
    cursor = cnt

print(datas)
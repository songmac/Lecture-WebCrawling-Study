from selenium import webdriver
import json
import time

chromedriver = 'c:/webdriver/chromedriver'
driver = webdriver.Chrome(chromedriver)

# div#post div
driver.implicitly_wait(5)
driver.get('https://crawlingstudy-dd3c9.web.app/05/')

lists = driver.find_elements_by_css_selector('div#post > div')

all_data = []

seq = 1
for idx in range(0, len(lists), 2):      
    
    lists[idx].click()
    time.sleep(0.5)

    data = {
        'id': seq,
        'title': lists[idx].text,
        'comments': []
    }

    comments = driver.find_elements_by_css_selector(f'#\\3{seq} > div')
    
    for idx2 in range(1, len(comments), 2):
        data['comments'].append(comments[idx2].text)
        
    all_data.append(data)
    seq += 1
    
with open('data.json', 'w') as json_file:
    json.dump(all_data, json_file)
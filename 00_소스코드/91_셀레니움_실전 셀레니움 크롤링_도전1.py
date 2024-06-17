from selenium import webdriver
import json
import time
import boto3

s3 = boto3.resource('s3')

chromedriver = 'c:/webdriver/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003&date=20211128')

news_all = []

items = driver.find_elements_by_css_selector("div.list_body > ul > li")
item_cnt = len(items)

for i in range(item_cnt):
    items = driver.find_elements_by_css_selector("div.list_body > ul > li")    
    items[i].find_element_by_css_selector("a").click()        
    time.sleep(1)  
    
    news_data = {
        'likeit': [],
        'reply': []
    }        
    
    try:
        news_data['title'] = driver.find_element_by_css_selector("h3#articleTitle").text
        news_data['body'] = driver.find_element_by_css_selector("div#articleBodyContents").text.strip().replace('\n','')
    except:
        
        try:
            news_data['title'] = driver.find_element_by_css_selector("h3.title").text
            news_data['body'] = driver.find_element_by_css_selector("div#newsEndContents").text.strip().replace('\n','')
        except:
            news_data['title'] = driver.find_element_by_css_selector("h2.end_tit").text
            news_data['body'] = driver.find_element_by_css_selector("div#articleBody").text.strip().replace('\n','')
    
    
    try:
    
        driver.find_element_by_css_selector("#main_content > div.article_header > div.article_info > div > div.article_btns > div.article_btns_left > div > a").click()    
                                            
        for like in driver.find_elements_by_css_selector("div.article_btns_left ul.u_likeit_layer > li.u_likeit_list"):
            news_data['likeit'].append({
                'name': like.find_element_by_css_selector("span.u_likeit_list_name").text,
                'count': like.find_element_by_css_selector("span.u_likeit_list_count").text
            })
        
        try:
            driver.find_element_by_css_selector("#cbox_module > div.u_cbox_wrap.u_cbox_ko.u_cbox_type_sort_favorite > div.u_cbox_view_comment > a").click()    
            time.sleep(0.5)     
            #while True:
            
            idx = 0
            
            for i in range(2):
                
                reply = driver.find_elements_by_css_selector("#cbox_module_wai_u_cbox_content_wrap_tabpanel > ul > li")
                print(i)
                try:
                    for i in range(idx, len(reply)):
                        try:
                            news_data['reply'].append(reply[i].find_element_by_css_selector("span.u_cbox_contents").text.strip())
                        except:
                            pass
                        
                    driver.find_element_by_css_selector("#cbox_module > div.u_cbox_wrap.u_cbox_ko.u_cbox_type_sort_favorite > div.u_cbox_paginate > a").click()    
                    time.sleep(0.2)
                except:
                    break
                
                idx = len(reply)
                
            driver.back()
            time.sleep(0.3)
                
        except:
            pass
        
        driver.back()
        time.sleep(0.3)
    
    except:
        pass
    
    news_all.append(news_data)
    
    driver.back()
    time.sleep(0.3)
    
        
s3.Bucket('study-012314').put_object(Key=f'selenium/news.json', Body=json.dumps(news_all, ensure_ascii=False))
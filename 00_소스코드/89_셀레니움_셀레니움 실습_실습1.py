from selenium import webdriver

chromedriver = 'c:/webdriver/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://crawlingstudy-dd3c9.web.app/03/')

popular = []

for item in driver.find_elements_by_css_selector("ul#popularItemList li"):
    popular.append([item.find_element_by_css_selector("a").text,
                    item.find_element_by_css_selector("span").text.replace(",","")])
    
lst_major = []

for item in driver.find_elements_by_css_selector("ul.lst_major li"):
    lst_major.append([item.find_element_by_css_selector("a").text,
                    item.find_element_by_css_selector("span").text.replace(",","")])
    
print(popular)
print(lst_major)
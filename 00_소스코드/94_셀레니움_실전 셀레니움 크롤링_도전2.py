from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='study', passwd='study', db='study')
cursor = db.cursor()

chromedriver = 'c:/webdriver/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.rocketpunch.com/jobs?')

time.sleep(3)

for now_page in range(1, 11):    
    
    for page in driver.find_elements_by_css_selector("#search-results > div.ui.blank.right.floated.segment > div > div.tablet.computer.large.screen.widescreen.only > a"):
        
        if page.text == str(now_page):
            page.send_keys(Keys.ENTER)
            time.sleep(3)
            
            print(len(driver.find_elements_by_css_selector("div#company-list div.company")))
            for company in driver.find_elements_by_css_selector("div#company-list div.company"):
                
                sql = """
                    INSERT INTO company(name, description)
                         VALUES (%s, %s)
                """
                
                cursor.execute(sql, (company.find_element_by_css_selector("h4.name > strong").text.strip(),
                                     company.find_element_by_css_selector("div.description").text.strip()))
                
                db.commit()
                company_id = cursor.lastrowid
                
                try:
                    more = company.find_element_by_css_selector("a.more-jobs")
                    driver.execute_script("arguments[0].click()", more)
                except:
                    pass
                
                for jobdetail in company.find_elements_by_css_selector("div.company-jobs-detail .job-detail"):
                    
                    sql = """
                        INSERT INTO JOB(company_id, title, info, date)
                                 VALUES(%s, %s, %s, %s)
                    """
                    
                    cursor.execute(sql, (company_id,
                                         jobdetail.find_element_by_css_selector("a").text.strip(),
                                         jobdetail.find_element_by_css_selector("span.job-stat-info").text.strip(),
                                         jobdetail.find_element_by_css_selector("div.job-dates > span").text.strip()))
            
            print('이동')
            break
            
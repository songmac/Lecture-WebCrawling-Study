from bs4 import BeautifulSoup
import requests
import json
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='study', passwd='study', db='study')
cursor = db.cursor()

for page in range(1, 11):
    
    print(page)
    
    response = requests.get(f'https://www.rocketpunch.com/api/jobs/template?page={page}&q=')
    soup = BeautifulSoup(response.json()['data']['template'], 'html.parser')

    for company in soup.select('div#company-list > div.company'):
        name = company.select_one('div.company-name h4 strong').text
        description = company.select_one('div.description').text #.replace('🚀','').replace('✨','')
            
        print(name)
        print(description)
        
        cursor.execute("""
            INSERT INTO company(name, description)
            VALUES (%s, %s)
        """, (name, description))

        db.commit()        
        company_id = cursor.lastrowid
            
        for detail in company.select('div.company-jobs-detail > div.job-detail'):
            title = detail.select_one('a').text.strip()
            info = detail.select_one('span.job-stat-info').text.strip()
            date = detail.select_one('div.job-dates > span').text.strip()
            
            job_detail_sql = """
                INSERT INTO job(company_id, title, info, date)
                     VALUES (%s, %s, %s, %s)
            """
           
                        
            cursor.execute(job_detail_sql, (company_id, title, info, date))
            db.commit()
        
        print('')
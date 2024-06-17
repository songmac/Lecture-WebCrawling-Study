import requests
import pymysql
from bs4 import BeautifulSoup

response = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
soup = BeautifulSoup(response.text, 'html.parser')

db = pymysql.connect(host='localhost', port=3306, user='study', passwd='study', db='study', charset='utf8')
cursor = db.cursor()

for idx, movie in enumerate(soup.select('table.list_ranking tr > td.title a')):
    
    sql = f"""
        INSERT INTO MOVIE
        VALUES ({idx + 1}, '{movie.text}')
    """    
    cursor.execute(sql)
    db.commit()
    #print(idx + 1, movie.text)
    
cursor.close()
db.close()

import requests
import datetime
import boto3
import json
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'
}

s3 = boto3.resource('s3')

date = datetime.datetime.strptime('20211123', '%Y%m%d')

for i in range(7):

    date_str = date.strftime('%Y%m%d')
    news = []
    page = 1

    while True:    
        
        print(date_str, page)    

        url = f'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003&date={date_str}&page={page}'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        if str(page) != soup.select_one("div.paging strong").text.strip():
            break

        for news_data in soup.select("ul.type06 li"):
            news.append({
                'title': news_data.select('a')[-1].text.strip(),
                'body': news_data.select_one('span.lede').text.strip()
            })
            
        page += 1
        
    s3.Bucket('bucket').put_object(Key=f'news/{date_str}.json', Body=json.dumps(news, ensure_ascii=False))
    date = date - datetime.timedelta(days=1)
    
    
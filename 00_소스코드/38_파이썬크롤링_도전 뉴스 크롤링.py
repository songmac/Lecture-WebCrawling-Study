import requests
import datetime
from bs4 import BeautifulSoup

date = datetime.datetime.strptime('20211120', '%Y%m%d')
page = 1

for i in range(20):
    
    print("=============================================")
    print("=============== 날짜 : ", date.strftime('%Y%m%d'))
    print("=============================================")

    while True:

        date_str = date.strftime('%Y%m%d')
        URL = f'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003&date={date_str}&page={page}'

        headers = {  
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print("=============================================")
        print("=============== 현재 페이지 : ", page)
        print("=============================================")
        
        if str(page) != soup.select_one('div.paging > strong').text:
            print('크롤링완료')
            break

        for news_item in soup.select('div.list_body ul li'):    
            #print(news_item.select('dt')[1].select_one('a').text.strip())
            
            news_url = ''
            
            try:
                news_url = news_item.select('dt')[1].select_one('a').attrs['href']
            except:
                news_url = news_item.select('dt')[0].select_one('a').attrs['href']
                
            response = requests.get(news_url, headers=headers)            
            news_soup = BeautifulSoup(response.text, 'html.parser')
            
            title = ''
            body = ''
            
            try:
                # 일반기사
                title = news_soup.select_one('div.article_info h3#articleTitle').text.strip()       
                body = news_soup.select_one('div.article_body div#articleBodyContents').text.strip().replace('\n','')
            except:
                
                try:
                    # 스포츠기사
                    title = news_soup.select_one('div.news_headline h4.title').text.strip()
                    body = news_soup.select_one('div#newsEndContents').text.strip().replace('\n','')
                    
                except:
                    #연예기사
                    title = news_soup.select_one('div.end_ct_area h2.end_tit').text.strip()
                    body = news_soup.select_one('div.end_body_wrp div#articeBody').text.strip().replace('\n','')
                    
            
            print(title)
            print('')
            print(body)
            print('')
            print('')
        
        page += 1


    date = date - datetime.timedelta(days=1)
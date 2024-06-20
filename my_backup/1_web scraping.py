import requests
from bs4 import BeautifulSoup

URL = 'https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&ssc=tab.nx.all&query=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&oquery=%EC%98%81%ED%99%94&tqi=iFZ%2BNdqo1aVssu%2B4ZOhssssstzV-222396&acq=%EC%98%81%ED%99%94&acr=2&qdt=0'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

movie = []
        
for item in soup.select('#main_pack ._panel_popular._tab_content ul._panel li'):
    movie.append({
        '순위' : item.select_one('.thumb span.this_text').text,
        '제목' : item.select_one('.title_box strong.name').text,
        '관객 수' : item.select_one('.title_box span.sub_text').text
    })

print(movie)

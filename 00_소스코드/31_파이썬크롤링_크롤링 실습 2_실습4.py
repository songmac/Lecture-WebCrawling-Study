import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

apt = []

for item in soup.select('.sale_list li'):
    
    apt.append({
        '이름': item.select_one('.sale_tit').text.strip(),
        '보증금': item.select('.detail_info dd.txt')[0].select_one('strong').text.replace(',',''),
        '유형': item.select('.detail_info dd.txt')[1].text.split('|')[0],
        '분양유형': item.select('.detail_info dd.txt')[1].text.split('|')[1],
        '세대수': item.select('.detail_info dd.txt')[2].text.split('|')[0],
        '평형': item.select('.detail_info dd.txt')[2].text.split('|')[1],
    })
    
    
print(apt)
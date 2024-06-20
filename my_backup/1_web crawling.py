import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

start_url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003&date=20240618'
response = requests.get(start_url)
soup = BeautifulSoup(response.text, 'html.parser')

news_links = []

# 뉴스 링크 수집
for a_tag in soup.select('.list_body ul li dt.photo a'):
    news_links.append(a_tag.attrs['href'])

news_data = []

# 각 링크를 순회하며 제목과 본문 추출
for link in news_links:
    news_url = urljoin(start_url, link)
    response = requests.get(news_url)
    news_soup = BeautifulSoup(response.text, 'html.parser')

    title = news_soup.select_one('#title_area span').text
    body = news_soup.select_one('#newsct_article #dic_area').text.strip()

    news_data.append({
        'title': title,
        'body': body
    })

print(news_data)

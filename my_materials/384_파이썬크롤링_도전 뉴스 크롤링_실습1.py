import requests
from bs4 import BeautifulSoup

URL = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# 각 뉴스 기사의 링크를 저장할 리스트
news_links = []

# 모든 li 태그 내의 a 태그 링크를 추출
for a_tag in soup.select('#main_content ul li dt.photo a'):
    news_links.append(a_tag.attrs['href'])

# 각 링크에 접근하여 제목과 본문을 추출
for link in news_links:
    new_response = requests.get(link)
    new_soup = BeautifulSoup(new_response.text, 'html.parser')

    # 뉴스 타이틀 출력
    title = new_soup.select_one('#title_area span').text
    print(title)

    # 뉴스 본문 출력
    for item in new_soup.select('#newsct_article #dic_area'):
        for em in item.select('em'): # extract() 메서드를 사용하여 <em> 태그를 제거한 후 텍스트를 추출
            em.extract()
        print(item.text.strip())
        # print("\n" + "="*80 + "\n")
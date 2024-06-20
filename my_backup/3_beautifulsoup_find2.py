from bs4 import BeautifulSoup
import requests

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
p = soup.find("p")
p_all = soup.find_all("p", limit=2)

print(p.text)

# 리스트 내 각 요소의 텍스트를 추출하여 출력
for paragraph in p_all:
    print(paragraph.text)

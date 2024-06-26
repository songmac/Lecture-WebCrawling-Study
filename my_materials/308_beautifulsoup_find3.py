from bs4 import BeautifulSoup
import requests

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# a 태그 내 내용과 href속성의 속성 값 추출
a = soup.find("a")
print(a.text)
print(a.attrs["href"])

# table 태그와 tbody 태그의 내용 추출
result = soup.find("table")
result2 = result.find("tbody")
print(result.text)
print(result2.text)



"""
# class속성의 속성값 출력
thead = soup.find("thead")
tr_head = thead.find("tr")
ths = tr_head.find_all("th")

for th in ths:
    class_attr = th.attrs.get("class", "No class attribute")
    print(class_attr[0])  # 리스트의 첫 번째 요소를 출력

"""
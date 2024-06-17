import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

popular = []
major = []

for item in soup.select("#popularItemList li"):
    popular.append([item.select_one("a").text, item.select_one("img").attrs['alt']])
    
print(popular)

for item in soup.select("ul.lst_major li"):
    major.append([item.select_one("a").text, item.select_one("img").attrs['alt']])    

print(major)    

import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/03/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

popular = []
major = []

for item in soup.select("#popularItemList li"):    
    if item.select_one('img').attrs['alt'] == '상한':
        popular.append([item.select_one('a').text, item.select_one('span').text])
        
for item in soup.select(".lst_major li"):
    if item.select_one('img').attrs['alt'] == '상한':
        major.append([item.select_one('a').text, item.select_one('span').text])
        
print(popular)
print(major)
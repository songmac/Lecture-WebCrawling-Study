import requests
from bs4 import BeautifulSoup

URL = 'http://movie.naver.com/movie/sdb/rank/rmovie.naver'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
for i, movie in enumerate(soup.select('table.list_ranking tr > td.title a')):
    print(i + 1, movie.text.strip())
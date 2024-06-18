import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

for atag in soup.find_all('a'):
    new_url = URL + atag.attrs['href'] # attr 아님
    response = requests.get(new_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup.find('p').text.strip()) # find 먼저 하고 text를 추출해야 함
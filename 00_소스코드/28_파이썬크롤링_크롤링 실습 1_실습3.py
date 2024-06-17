import requests
from bs4 import BeautifulSoup

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

for atag in soup.find_all('a'):
    response = requests.get('https://crawlingstudy-dd3c9.web.app/01/' + atag.attrs['href'])
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.find('p').text.strip())
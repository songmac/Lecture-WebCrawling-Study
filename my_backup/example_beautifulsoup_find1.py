from bs4 import BeautifulSoup
import requests

URL = 'https://crawlingstudy-dd3c9.web.app/01/'
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("title")

print(title)
print(title.text)



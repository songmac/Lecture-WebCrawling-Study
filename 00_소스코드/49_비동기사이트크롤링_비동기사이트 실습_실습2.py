import requests
import re
import json
from bs4 import BeautifulSoup

all_news = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

response = requests.get("https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&oid=003", headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

for news_item in soup.select("ul.type06_headline li"):   
        
    #url = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=101&oid=011&aid=0003987613"
    url = news_item.select_one("a").attrs['href']
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser') 

    oid = re.search("(?<=oid=)[0-9]+", url).group()
    aid = re.search("(?<=aid=)[0-9]+", url).group()

    response = requests.get(f"https://news.like.naver.com/v1/search/contents?suppress_response_codes=true&q=NEWS%5Bne_{oid}_{aid}%5D%7CNEWS_SUMMARY%5B{oid}_{aid}%5D%7CJOURNALIST%5B69146(period)%5D%7CNEWS_MAIN%5Bne_{oid}_{aid}%5D&isDuplication=false&cssIds=MULTI_PC_SSL%2CNEWS_PC_SSL&_=1637846808499")

    news = {
        'title': soup.select_one("div.article_info h3#articleTitle").text.strip(),
        'content': soup.select_one("div.article_body div#articleBodyContents").text.strip(),
        'reaction': {
            'sad': 0,
            'like': 0,
            'warm': 0,
            'want': 0,
            'angry': 0
        },
        'comments': []
    }

    for reaction in response.json()['contents'][0]['reactions']:
        news['reaction'][reaction['reactionType']] = reaction['count']

    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'NNB=3VKMCDRPPQVWC; nx_ssl=2; ASID=7d8f048e0000017cfb2340b50000005e',
        'referer': 'https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=101&oid=011&aid=0003987613&m_view=1&includeAllCount=true&m_url=%2Fcomment%2Fall.nhn%3FserviceId%3Dnews%26gno%3Dnews011%2C0003987613%26sort%3Dlikability',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    response = requests.get(f"https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_economy&pool=cbox5&_wr&lang=ko&country=KR&objectId=news{oid}%2C{aid}&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=1&refresh=false&sort=FAVORITE&current=2682236263&prev=2682084903&moreParam.direction=next&moreParam.prev=00004i00005600000018cudyf&moreParam.next=00000100000100000018cxmqv&includeAllStatus=true&_=1637848076231", headers=headers)
    lastpage = json.loads(response.text.replace('_callback(','')[:-2])['result']['pageModel']['lastPage']

    for page in range(1, lastpage + 1):
        response = requests.get(f"https://apis.naver.com/commentBox/cbox/web_naver_list_jsonp.json?ticket=news&templateId=default_economy&pool=cbox5&_wr&lang=ko&country=KR&objectId=news{oid}%2C{aid}&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page={page}&refresh=false&sort=FAVORITE&current=2682236263&prev=2682084903&moreParam.direction=next&moreParam.prev=00004i00005600000018cudyf&moreParam.next=00000100000100000018cxmqv&includeAllStatus=true&_=1637848076231", headers=headers)
        for comment in json.loads(response.text.replace('_callback(','')[:-2])['result']['commentList']:
            news['comments'].append(comment['contents'].strip())
            
    all_news.append(news)
      
with open('news.json', 'w', encoding='utf8') as json_file:
    json.dump(all_news, json_file, ensure_ascii=False)
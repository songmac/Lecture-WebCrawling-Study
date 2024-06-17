import requests
import re
from bs4 import BeautifulSoup

for i in range(1,11):
    
    print('PAGE ======================= ', i)

    URL = f'https://search.musinsa.com/category/001?d_cat_cd=001&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page={i}&display_cnt=90&sale_goods=&group_sale=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&shoeSizeOption=&tags=&campaign_id=&timesale_yn=&q=&includeKeywords=&measure='
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'html.parser')
    for item in soup.select('ul#searchList > li'):
        #print('브랜드 : ', item.select_one('.article_info p.item_title').text.strip())
        print('상품명 : ', item.select_one('.article_info p.list_info a').attrs['title'])
        #print('상품명 : ', re.sub('[0-9]{1,2}\/[0-9]{1,2} 배송', '', item.select_one('.article_info p.list_info a').text).strip())
        
        price = ''
        
        # if len(item.select_one('.article_info p.price').text.strip().split(" ")) == 1:
        #     price = item.select_one('.article_info p.price').text.strip().split(" ")[0]
        # else:
        #     price = item.select_one('.article_info p.price').text.strip().split(" ")[1]
            
        if len(re.findall('[0-9,]*원', item.select_one('.article_info p.price').text)) == 1:
            price = re.findall('[0-9,]*원', item.select_one('.article_info p.price').text)[0]
        else:
            price = re.findall('[0-9,]*원', item.select_one('.article_info p.price').text)[1]
        
        print('가격 : ', price)
        print('')


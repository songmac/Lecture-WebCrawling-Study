import requests
import boto3
import json
from urllib import parse

search_text = '스파이더맨'
texts = []

s3 = boto3.resource('s3')

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language':'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'mid=YaJpSAALAAEjMtzol793-qrlfuQH; ig_did=D3373077-7E74-42BB-9FF3-6F1D3DDBB93A; ig_nrcb=1; csrftoken=R8FlC9Bg1vJwDF113EBnmyxMnGWMbq6p; ds_user_id=2210860117; sessionid=2210860117%3AvHzGtEDzXoaZhV%3A17; shbid="10360\0542210860117\0541669569854:01f7969a1b2ccdd110f348461e44c5725e9291ee3161176d749115729f67e9c645523c65"; shbts="1638033854\0542210860117\0541669569854:01f7fb4b18a07bba7d38aac0fd4ba77983755923d1a1fae82b9e63a276f40ae9b4d4583e"; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=74bQ4KjzFIIWW1EnUkZsFESPe23tw9Ya3rHauRlcu5s.eyJ1c2VyX2lkIjoiMTAwMDAwOTcxNjIyODI1IiwiY29kZSI6IkFRQUtzWjRvaUVEd0xSZzVLWEJPaFJUT1IyNU5OVjMxU1hmVFNySjhuenNraTdHcjFmbVM0YWIzNExKa3JhcndYOE9raFp3Y1AwbWpPdXNQRzR1QkVvZGRQRlNWWEdMd1JSRWgwQnpiVUpKbThKbjlvRjFyZlBvUEoyWW5OaDFrNG9pMnUyRU02TkNjc3ZKSXFLa0g3M2pDZVdORktRUWRZa1BMRHJDdnJtVXExdWkzVTQ5b1BxV1plUkZnYkdmQ1JfVG15QTlOdVg0bDB1cnpna3pNaVJsOWpoVU12RUlEcmdBakhJLW9iYXV0a0VuR19xU3dpR1pubWs4c0tQTTFoTEVHRng5cm9EQnFMU1lDWHlxMG92OGppNnJIYVFoYlU1bWNaUElzZ0JnWkNSQ1I0UkNNRlBmZ3h6Y1JhUHNzYWt2T0VOczNzeWJFS2hSNld0VTNyQ2gxIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQURsMHdqeFpCcW1xdVZGcGVlWFpCbjdmWkFQdUp5UWNzSVgyQjFGNDMzeGU1VXVpSEJiMXd0a1ZaQmxaQmFpdXhRVUtyVkVFQ2d6WkNlQVpBUzUwWkJiWkNQOUxPZkd4Qm9IRlE1U3p6cURiVjhMMXpoWkNuVW43MFJaQk1pZVRyQjV6ZDlVMHFHRnFnWWFOMkRIS2gxbnhMOEpVNmJ0ZHpkYnpaQ3R4dmFOaWRIZjQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTYzODA1OTk2OH0; rur="EAG\0542210860117\0541669596210:01f7ee22f1c5b7d24dba895389b93bfcdf9533c2edc8edbda43797e034f7772f8f4a1463"',
    'referer': 'https://www.instagram.com/explore/tags/%EB%A9%94%ED%83%80%EB%B2%84%EC%8A%A4/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'x-asbd-id': '198387',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': 'hmac.AR3H6_al8bIoRhyljB4FYtMQ6Z_EpxLT4G5Sf-8-gGdgLges',
    'x-requested-with': 'XMLHttpRequest'
}

response = requests.get('https://www.instagram.com/explore/tags/' + parse.quote(search_text) + '/?__a=1', headers=headers)

# print(response.status_code)
# print(response.json()['data']['recent']['sections'])

for rows in response.json()['data']['recent']['sections']:
    for columns in rows['layout_content']['medias']:
        text = ''
        try:
            text = columns['media']['caption']['text']
        except:
            pass
        
        texts.append(text)
        
        if 'carousel_media' in columns['media']:
            #이미지 여러개
            for idx, image in enumerate(columns['media']['carousel_media']):
                res_image = requests.get(image['image_versions2']['candidates'][0]['url'])
                s3.Bucket('study-012314').put_object(Key=f'insta_search/{search_text}/{id}_{idx}.jpg', Body=res_image.content)
            pass
        else:
            #이미지 한개                
            res_image = requests.get(columns['media']['image_versions2']['candidates'][0]['url'])
            s3.Bucket('study-012314').put_object(Key=f'insta_search/{search_text}/{id}.jpg', Body=res_image.content)
            pass
        
headers = {
'accept': '*/*',
#'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
'content-length': '183',
'content-type': 'application/x-www-form-urlencoded',
'cookie': 'mid=YaJpSAALAAEjMtzol793-qrlfuQH; ig_did=D3373077-7E74-42BB-9FF3-6F1D3DDBB93A; ig_nrcb=1; csrftoken=R8FlC9Bg1vJwDF113EBnmyxMnGWMbq6p; ds_user_id=2210860117; sessionid=2210860117%3AvHzGtEDzXoaZhV%3A17; shbid="10360\0542210860117\0541669569854:01f7969a1b2ccdd110f348461e44c5725e9291ee3161176d749115729f67e9c645523c65"; shbts="1638033854\0542210860117\0541669569854:01f7fb4b18a07bba7d38aac0fd4ba77983755923d1a1fae82b9e63a276f40ae9b4d4583e"; fbm_124024574287414=base_domain=.instagram.com; fbsr_124024574287414=74bQ4KjzFIIWW1EnUkZsFESPe23tw9Ya3rHauRlcu5s.eyJ1c2VyX2lkIjoiMTAwMDAwOTcxNjIyODI1IiwiY29kZSI6IkFRQUtzWjRvaUVEd0xSZzVLWEJPaFJUT1IyNU5OVjMxU1hmVFNySjhuenNraTdHcjFmbVM0YWIzNExKa3JhcndYOE9raFp3Y1AwbWpPdXNQRzR1QkVvZGRQRlNWWEdMd1JSRWgwQnpiVUpKbThKbjlvRjFyZlBvUEoyWW5OaDFrNG9pMnUyRU02TkNjc3ZKSXFLa0g3M2pDZVdORktRUWRZa1BMRHJDdnJtVXExdWkzVTQ5b1BxV1plUkZnYkdmQ1JfVG15QTlOdVg0bDB1cnpna3pNaVJsOWpoVU12RUlEcmdBakhJLW9iYXV0a0VuR19xU3dpR1pubWs4c0tQTTFoTEVHRng5cm9EQnFMU1lDWHlxMG92OGppNnJIYVFoYlU1bWNaUElzZ0JnWkNSQ1I0UkNNRlBmZ3h6Y1JhUHNzYWt2T0VOczNzeWJFS2hSNld0VTNyQ2gxIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQURsMHdqeFpCcW1xdVZGcGVlWFpCbjdmWkFQdUp5UWNzSVgyQjFGNDMzeGU1VXVpSEJiMXd0a1ZaQmxaQmFpdXhRVUtyVkVFQ2d6WkNlQVpBUzUwWkJiWkNQOUxPZkd4Qm9IRlE1U3p6cURiVjhMMXpoWkNuVW43MFJaQk1pZVRyQjV6ZDlVMHFHRnFnWWFOMkRIS2gxbnhMOEpVNmJ0ZHpkYnpaQ3R4dmFOaWRIZjQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTYzODA1OTk2OH0; rur="EAG\0542210860117\0541669596247:01f76ef0c5a5c0650588062420a373bdf84bb137ba29ebfe24bb120862adfc495d163013"',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'R8FlC9Bg1vJwDF113EBnmyxMnGWMbq6p',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': 'hmac.AR3H6_al8bIoRhyljB4FYtMQ6Z_EpxLT4G5Sf-8-gGdgLges',
'x-instagram-ajax': '038693313a95'
}

page = 1
max_id = 'QVFDekJYOXhTZ3hJRy1MZDQ2bnozZ3NBWVAwbEF0TEtUa3pFNnFUS05CeEVFLVBYM2pMQkdQb19hbzdzN2VINGVRci13aE5nb09HX0ZYZXFpTnZUR1NoRg=='

for page in range(5):
            
    data = {
        'include_persistent': 0,
        'max_id': max_id,
        'page': page,
        'surface': 'grid',
        'tab': 'recent'
    }

    url = 'https://i.instagram.com/api/v1/tags/' + parse.quote(search_text) +'/sections/'
    response = requests.post(url, data=data, headers=headers)

    for rows in response.json()['sections']:
        
        for columns in rows['layout_content']['medias']:
            id = columns['media']['id']
            text = ''
            try:
                text = columns['media']['caption']['text']
            except:
                pass
            
            texts.append(text)
            
            if 'carousel_media' in columns['media']:
                #이미지 여러개
                for idx, image in enumerate(columns['media']['carousel_media']):
                    res_image = requests.get(image['image_versions2']['candidates'][0]['url'])
                    s3.Bucket('study-012314').put_object(Key=f'insta_search/{search_text}/{id}_{idx}.jpg', Body=res_image.content)
                pass
            else:
                #이미지 한개                
                res_image = requests.get(columns['media']['image_versions2']['candidates'][0]['url'])
                s3.Bucket('study-012314').put_object(Key=f'insta_search/{search_text}/{id}.jpg', Body=res_image.content)
                pass
            
    max_id = response.json()['next_max_id']
    page = response.json()['next_page']
    
s3.Bucket('study-012314').put_object(Key=f'insta_search/{search_text}.json', Body=json.dumps(texts, ensure_ascii=False))
print('완료')
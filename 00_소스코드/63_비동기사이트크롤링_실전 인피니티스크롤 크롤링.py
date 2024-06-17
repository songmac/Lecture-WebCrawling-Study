import requests
import json

main_list = []

magazineOffset = 0
contestOffset = 0
exhibitOffset = 0
galleryOffset = 0

for i in range(10):
    response = requests.get(f'https://www.jungle.co.kr/recent.json?magazineOffset={magazineOffset}&contestOffset={contestOffset}&exhibitOffset={exhibitOffset}&galleryOffset={galleryOffset}')
    response_json = response.json()

    for item in response_json['moreList']:
        main_list.append(
            {
                'title': item['title'],
                'cagegory': item['targetCode']
            }
        )

    magazineOffset = response_json['magazineOffset']
    contestOffset = response_json['contestOffset']
    exhibitOffset = response_json['exhibitOffset']
    galleryOffset = response_json['galleryOffset']

with open('main_list.json', 'w', encoding='utf8') as json_file:
    json.dump(main_list, json_file, ensure_ascii=False)
import requests
import json

# JSON 데이터 가져오기
response = requests.get("https://jsonplaceholder.typicode.com/posts")
json_data = response.text

# JSON 데이터를 python 객체로 변환
data = json.loads(json_data)

# 첫 번째 포스트의 제목 출력
print(data[0]['title'])






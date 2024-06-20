import requests

# POST 요청을 보낼 URL (API end point)
url = 'https://jsonplaceholder.typicode.com/posts'

# 요청에 포함할 헤더
headers = {
    'Content-Type': 'application/json',
}

# 요청 본문에 포함할 데이터
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# POST 요청 보내기
response = requests.post(url, headers=headers, json=data)

# 응답 상태 코드 출력
print(f'Status Code: {response.status_code}')

# 응답 본문 출력
print(f'Response Body: {response.json()}')





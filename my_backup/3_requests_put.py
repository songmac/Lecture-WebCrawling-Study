import requests

# PUT 요청을 보낼 URL (업데이트할 자원의 ID 포함)
url = 'https://jsonplaceholder.typicode.com/posts/1'

# 요청에 포함할 헤더
headers = {
    'Content-Type': 'application/json',
}

# 요청 본문에 포함할 데이터 (업데이트할 데이터)
data = {
    'id': 1,  # 자원의 ID는 업데이트할 자원의 고유 식별자
    'title': 'updated title',
    'body': 'updated body',
    'userId': 1
}

# PUT 요청 보내기
response = requests.put(url, headers=headers, json=data)

# 응답 상태 코드 출력
print(f'Status Code: {response.status_code}')

# 응답 본문 출력
print(f'Response Body: {response.json()}')



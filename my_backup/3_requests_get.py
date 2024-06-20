import requests

# GET 요청을 보낼 URL (test용 무료 API)
url = 'https://jsonplaceholder.typicode.com/posts/1'

# GET 요청 보내기
response = requests.get(url)

# 응답 상태 코드 출력
print(f'Status Code: {response.status_code}')

# 응답 본문 출력 (json형식으로 출력)
print(f'Response Body: {response.json()}')



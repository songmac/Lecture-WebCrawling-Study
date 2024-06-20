import requests

# GET 요청을 보낼 URL (test용 무료 API)
url = 'https://jsonplaceholder.typicode.com/posts/1'

# GET 요청 보내기
response = requests.get(url)

# 응답 상태 코드 출력
print(f'Status Code: {response.status_code}')

# 응답 본문 출력 (json형식으로 출력)
print(f'Response Body: {response.json()}')




"""
# POST 요청을 보낼 URL
url_post = 'https://jsonplaceholder.typicode.com/posts'

# 요청에 포함할 헤더
headers = {
    'Content-Type': 'application/json',
}

# 요청 본문에 포함할 데이터
data_post = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# POST 요청 보내기
response_post = requests.post(url_post, headers=headers, json=data_post)

# 응답 상태 코드 출력
print(f'POST Request - Status Code: {response_post.status_code}')

# 응답 본문 출력
print(f'POST Request - Response Body: {response_post.json()}')

# PUT 요청을 보낼 URL (업데이트할 자원의 ID 포함)
url_put = 'https://jsonplaceholder.typicode.com/posts/1'

# 요청 본문에 포함할 데이터 (업데이트할 데이터)
data_put = {
    'id': 1,
    'title': 'updated title',
    'body': 'updated body',
    'userId': 1
}

# PUT 요청 보내기
response_put = requests.put(url_put, headers=headers, json=data_put)

# 응답 상태 코드 출력
print(f'PUT Request - Status Code: {response_put.status_code}')

# 응답 본문 출력
print(f'PUT Request - Response Body: {response_put.json()}')

# DELETE 요청을 보낼 URL (삭제할 자원의 ID 포함)
url_delete = 'https://jsonplaceholder.typicode.com/posts/1'

# DELETE 요청 보내기
response_delete = requests.delete(url_delete)

# 응답 상태 코드 출력
print(f'DELETE Request - Status Code: {response_delete.status_code}')

# 응답 본문 출력
print(f'DELETE Request - Response Body: {response_delete.text}')
"""
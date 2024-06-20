import requests

# DELETE 요청을 보낼 URL (삭제할 자원의 ID 포함)
url = 'https://jsonplaceholder.typicode.com/posts/1'

# DELETE 요청 보내기
response = requests.delete(url)

# 응답 상태 코드 출력
print(f'Status Code: {response.status_code}')

# 응답 본문 출력
print(f'Response Body: {response.text}')  # DELETE 요청의 경우 응답 본문이 비어 있을 수 있음

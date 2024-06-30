import requests
import json

# JSONPlaceholder API로부터 사진 데이터를 가져옴
# 비동기 웹사이트의 예시로 JSONPlaceholder API를 사용하는 것은 적절하지 않을 수 있음.
# JSONPlaceholder는 정적 JSON 데이터를 제공하는 REST API로, 비동기 웹사이트의 동작을 보여주는 데는 한계가 있음.
response = requests.get('https://jsonplaceholder.typicode.com/photos')
photos = response.json()

# 데이터를 저장할 리스트 초기화함
datas = []

# 각 사진 데이터를 순회함
for photo in photos:
    # 각 사진 데이터의 id와 title을 저장하고 comment를 빈 리스트로 초기화함
    temp = {
        'id': photo['id'],
        'title': photo['title'],
        'comment': []
    }
    
    # 관련 코멘트 데이터를 가져옴
    # 여기서 params 매개변수는 GET 요청의 쿼리 문자열을 정의함.
    # 'postId' 파라미터를 사용하여 특정 포스트에 해당하는 코멘트를 필터링함.
    # https://jsonplaceholder.typicode.com/comments?postId=1 같은 URL이 생성됨.
    comments_response = requests.get('https://jsonplaceholder.typicode.com/comments', params={'postId': photo['id']})
    comments = comments_response.json()
    
    # 각 코멘트의 본문을 temp 딕셔너리의 comment 리스트에 추가함
    temp['comment'].extend(comment['body'] for comment in comments)
    
    # 완성된 temp 딕셔너리를 datas 리스트에 추가함
    datas.append(temp)

# 최종 데이터를 JSON 파일로 저장함
with open("data.json", "w") as json_file:
    json.dump(datas, json_file, ensure_ascii=False, indent=4)

# 최종 데이터를 출력함
print(datas)



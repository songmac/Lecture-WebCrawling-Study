import re

text = """
<p>
<span>네이버가 뉴스 서비스에 인공지<br>능(AI)을 도입해 페이지 뷰(PV)를 늘리고 이용자를 끌어 모으고 있다.</span>
<span>네이버는 5일 오전 서울 강남구 그랜드 인터컨티넨털 호텔에서 AI 콜로키움 2019를 열고 이 같은 AI 성과와 전략을 소개했다.</span>
<span>이날 기조연설에서 김광현 네이버 서치앤클로바 리더는 "AI 뉴스 추천 시스템인 에어스(AiRS)를 도입하면서 뉴스 소비량이 확대되고 있다" 고 말했다.</span>
</p>
"""

items = []

result = re.finditer("(?<=<span>)((?!<span>).)*(?=<\/span>)", text)

for item in result:
    items.append(item.group())
    
print(items)
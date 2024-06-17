import re

text = """
jkilee@gmail.com
kttredef@naver.com
akdef!aa.com
adekik@best.kr
abkereff@aacde
adefgree@korea.co.kr
"""

result = re.finditer("[a-zA-Z0-9]+@[a-zA-Z0-9]+(\.[a-zA-Z]{2,3}){1,2}", text)

for phone_number in result:
    print(phone_number.group())
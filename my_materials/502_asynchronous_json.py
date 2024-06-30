"""import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
result_dic = json.loads(response.text)

with open("data.json", "w") as json_file:
    json.dump(result_dic, json_file)"""


import json

with open("data.json", "r") as json_file:
    result = json.load(json_file)
    
print(result)




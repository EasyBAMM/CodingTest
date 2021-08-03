# book - Tct 개발형코딩테스트(웹 조회)

import requests

target = "https://google.com"
response = requests.get(url=target)
print(response.text)

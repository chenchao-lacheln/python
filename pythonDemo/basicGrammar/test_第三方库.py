import requests
r= requests.get("http://www.baidu.com")
print(r.text)
r.encoding = "UTF-8"
print(r.content)
print(r.json)
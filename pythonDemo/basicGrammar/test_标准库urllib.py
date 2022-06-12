import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
print(response.status) # 状态
print(response.read()) #响应体
print(response.headers) #获取头部信息

# 作为了解用，requests库相当于是对urllib做的一个封装升
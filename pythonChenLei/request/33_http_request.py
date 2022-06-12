import requests

# # get请求
# url = 'http://v.juhe.cn/laohuangli/d'
# res = requests.get(url,cookies=None)
# print(res)
# print("响应头：",res.headers)
# print("响应状态码：",res.status_code)
# print("响应正文：",res.text)


# post请求
url = 'http://v.juhe.cn/laohuangli/d'
data = {"key":"b6f5b113fd65d54afb564728cc045b68","date":"2021-08-15"}
res = requests.post(url,data)
print(res)
print("响应头：",res.headers)
print("响应状态码：",res.status_code)
print("响应正文：",res.text,type(res.text))
print("响应正文：",res.json,type(res.json))

#html xml json------>json会报错，只有json类型的返回值才支持json
# html和json格式不可以互相转换

# 34 15：51
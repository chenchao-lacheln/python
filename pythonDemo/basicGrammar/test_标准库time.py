import time

print(time.asctime())   # 获取国外的时间格式
print(time.time())  # 时间戳，公元纪年的秒数
print(time.localtime()) # 时间戳的元祖格式
print(time.strftime("%Y:%m:%d %H:%M:%S", time.localtime())) # 将当前时间戳转换成带格式的时间

# 获取两天前的时间
now_time = time.time()
two_day_before = now_time - 60*60*24*2
tuple_time = time.localtime(two_day_before)
print(time.strftime("%Y:%m:%d %H:%M:%S", tuple_time))

#获取三天后的时间
now_time = time.time()
three_day_after = now_time + 60*60*24*3
tuple_time = time.localtime(three_day_after)
print(time.strftime("%Y:%m:%d %H:%M:%S", tuple_time))
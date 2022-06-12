# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: Demo.py
# @Author: lacheln
# @Time: 9月 10, 2021
# ---

# 倒序排序


# 第一种方法:索引方法
list = [1,2,3,4,5]
new = list[2::-1] #取从下标为2的元素倒叙读取，"3"的下标为2，倒叙后则是[3,2,1]
print(new)

# 第二种方法
list = [1,2,3,4,5]
    # (1)第一种打印方式
list.reverse()
print(list)
    # 第二种打印方式
#为什么list.reverse()的返回值是None
#因为reverse()函数为了节省空间，把倒序的列表存入原始list中，直接改变了原始list的值，所以，调用此函数时什么都不会返回。
# list.reverse()
# new = list
# print(new)

#第三种方法
list = [1,2,3,4,5]
b = []
for i in reversed(list):
    b.append(i)
print(b)


# 去重
# 1.用循环查找的方式
list2 = [1,1,2,2,3,4,]
new_list = []
for i in list2:
    if i not in new_list:
        new_list.append(i)
print(new_list)

# 冒泡排序
a = [21,33,2,4,535,25,252,32,32,24,5,32]
for i in range(len(a)-1):
    for j in range(len(a)-1-i): #获取列表元素的索引值，第一个运行J=0
        if a[j] > a[j+1]: # 然后根据j和j+1比较大小
            a[j],a[j+1] = a[j+1],a[j]
print(a)

# 99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("{}X{}={} ".format(j,i,i*j),end='')
    print()
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: demo_yield.py
# @Author: lacheln
# @Time: 9月 08, 2021
# ---

# yield 原理 生成器
# 几个G的文件，我们需要读取她，可能会卡死，不能一下子全部读取，需要分开读取，一次读取一行数据
#定义一个生成器
def provider():
    for i in range(1,10):
        print("start reading")
        yield i #完成return 动作，帮我们返回数据,记录了上一次的执行位置，下一次的时候，继续在位置之后执行
        print(f"end reading{i}")

p = provider()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
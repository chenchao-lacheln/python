#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/15 9:40 下午
# @Author  : Lacheln

"""=================运行测试用例================="""
import pyDemo

'''
1.执行包下所有的用例: pyDemo/py.test [包名]
2.执行单独一个pytest模块: pyDemo 文件名.py
3.运行某个模块里面某个类:pytest文件名.py::类名
4.运行某个模块里面某个类里面的方法: pytest文件名.py::类名::方法名:
'''

"""
场景：执行失败的测试用例
命令行参数-使用缓存状态
"""
'''
--1f(--last-failed)只重新运行故障。
--ff(--failed- first) 先运行故障然后再运行其余的测试
'''

#pyDemo --lf -vs 会执行之前失败的测试用例，

# pytest执行后 会有失败的测试用例，再次执行pytest --lf -vs 会执行之前失败的测试用例，
# 如果上一次执行的测试用例成功了，没有失败的话，会执行所有的测试用例

#pyDemo --ff -vs 先运行失败的用例，再运行其他用例

"""=================常用命令行参数（使用pytest解释器执行用例）================="""

#场景：冒烟测试和回归测试
'-x 用例失败即停止 pyDemo xx.py -vs -x'

#场景：冒烟测试和回归测试  增加允许失败的个数
'--maxfail=20  允许失败20条，20条后停止  pyDemo xx.py -vs --maxfail=20'

'-m 标记用例'
'-k 执行包含某个关键字的测试用例  pyDemo xx.py -vs -k "str"    ' \
'也可以增加逻辑运算 pyDemo xx.py -vs -k "not str"不包含str关键字的'

'-v 打印详细日志'
'-s 打印输出日志,比如print()里面的打印内容 -vs通常一起使用'

#场景：测试平台中，使用pytest自动导入功能，先把用例收集上来，展示在前端界面，但是先不运行
'--collect-only 收集日志 不允许'

#pyDemo --help 查看帮助文档


"""=================使用python解释器执行用例================="""
#应用场景：测试平台开发和Jenkins 持续集成

# 使用pthon解释器的好处是：
# 1.直接使用pytest不通用，python解释器做判断既可以使用pytest脚本，也可以使用python脚本
# 2.方便指定python脚本 不同的用例可能对应的版本不一样

#第一种方式：使用main函数
## 正常情况 python3 xx.py是运行不了的，需要调取对应的方法再运行才生效 test_xx()调用方法后，再通过python运行
print(__name__) # __main__


@pyDemo.mark.android
def test_android():
    print("test android")
    assert 1 == 2
#ios
@pyDemo.mark.ios
def test_ios():
    print("test ios")
    assert 1 == 1
#web
@pyDemo.mark.web
def test_web():
    print("test weh")
    assert 2 == 2

# if __name__ == "__main__":
#     # 运行当前目录下的所有用例  执行命令： python3 test_run_case.py
#     pyDemo.main() #等价于pytest.main(['./])
#     # 执行某个文件下的某条用例
#     pyDemo.main(['test_run_case.py::test_web','-vs'])
#     # 运行某个标签
#     pyDemo.main(['test_run_case.py','-vs','-m','android'])
#第二种方式：python -m pyDemo xx.py



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/20 02:12
# @Author  : Lacheln

'''Allure基本介绍'''
# Allure是一个轻量级，灵活的，支持多语言的测试报告工具
# 多平台的,奢华的report框架
# 可以为dev/qa提供详尽的的测试报告、测试步骤、log
# 也可以为管理理层提供high level统计报告
# Java语言开发的，支持pytest, JaveScript, PHP, ruby等
# 可以集成到Jenkins

'''Allure环境安装'''
# 安装Java (推荐1.8版本)，需要配置环境变量
# 安装Allure,需要配置环境变量
# 2.13.8  Mac下载.tgz包
# https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.8/
#allure
# PATH="/Users/lacheln/software/allure-2.13.8/bin:${PATH}"
# export PATH
# allure --version

'''Allure 常用命令'''
#生成测试报告的流程
    # 运行pytest测试用例pytest --alluredir（生成中间结果，包括txt，json格式）
    #   执行allure serve 命令 生成在线版本测试报告
    #   执行allure generate 命令 生成最终版本测试报告


# 命令格式: allure [option] [ command ] [ command options ]
# 在测试执行期间收集结果
# pytest [ 测试文件] -s -q --alluredir=./result/ (--alluredir这个选项用于指定存储测试结果的路径)
# 查看测试报告
# 方式-:测试完成后查看实际报告，在线看报告， 会直接打开默认浏览器展示当前报告
    # allure serve . /result/ (注意这里的serve书写 )
# 方式二:从结果生成报告，这是一个启动tomcat的服务，需要两个步骤:生成报告，打开报告
    # 生成报告
        # allure generate ./result/ -o ./report/ --clean (注意:覆盖路径加--clean )
    # 打开报告
    # allure open -h 127 .0.0.1 -P 8883 ./report/


# 生成json等相关数据
    # pytest --alluredir ./result -vs
# 生成在线测试报告
    #  allure serve ./result
# 生成最终版本测试报告
# allure generate ./result

# 打开报告的方式(其他人也可以通过第二种方式，打开查看报告)
#     第一种是在idea中打开
#     第二种 allure open -h 127.0.0.1 -p 8883 ./allure-report/

# 清空 生成的 result 记录  --clean-alluredir
# pytest test_allure_title.py --alluredir ./result -vs --clean-alluredir


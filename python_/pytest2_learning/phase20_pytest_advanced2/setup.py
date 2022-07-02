#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/1 00:47
# @Author  : Lacheln


# setuptools构成工具，通过改工具的setup完成整个项目的构建
from setuptools import setup,find_packages
setup(
    # name 打包的名字
    name='pytest_encode',
    # 源码地址
    url='httpls;llgithub,com/xxx/pytest-encode',
    # 打包升级的版本
    version='1.0',
    # 作者
    author="xixi",
    # 邮箱
    author_email='418974188@qq.com',
    # 描述信息
    description='set your encoding and logger',
    # 完整的描述信息
    long_description='Show Chinese for your mark. parametrize(). Define logger variable . Define logger variable for getting your log',
    # 分类索引：可以增加pypi上被搜索到的几率
    classifiers=[#分类索引。pip 对所属包的分类
        'Framework :: Pytest', # 框架
        'Programming Language :: Python', # 使用语言
        'Topic :: Software Develosting', # 主题
        'Programming Language:: Python :: 3.pment :: Te8', # 开发语言和版本
    ],
    # 授权证书
    license= 'proprietary',
    # 可以通过import导包，通过 find_packages 可以找到所有的包
    packages = find_packages(), #['pytest_ encode'],
    # keywords 主要是便于pypi进行分类 包含项目的一些关键字
    keywords= [
        'pytest','py.test','pytest_encode',
    ],

    #需要安装的依赖，多个依赖用逗号隔开
    install_requires=[
        'pytest'
    ],
    #入口模块或者入口函数
    entry_points={
        'pytest11':[ # pytest11 是一个查找插件的关键字，查找插件所指定的主函数
            'pytest_encode = pytest_encode.main',
        ]
    },
    zip_safe=False # 针对Windows需要设置成False，否则会报错
)

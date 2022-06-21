#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/21 00:32
# @Author  : Lacheln

'''
场景:UI自动化用的比较多
希望在报告中看到测试用例的详细内容展示
比如在用例中添加附件信息，可以是数据，文本，图片，视频，网页
解决:
@allure.attach显示许多不同类型的提供的附件，可以补充测试，步骤或测试结果。
用法:
allure.attach(body(内容), name, attachment type, extension):
'''
import allure

@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤一：打开应用"):
            print("打开应用")
        with allure.step("步骤二：进入登录页面"):
            print("登录页面")
            allure.attach.file("/Users/lacheln/Pictures/1.jpg",
                               name="截图",
                               attachment_type = allure.attachment_type.JPG,
                               extension=".jpg")
        with allure.step("步骤三：输入用户信息"):
            allure.attach("这是一段文本信息",name="文本展示")
            print("输入用户名和密码")
        with allure.step("步骤四：进入成功页面"):
            allure.attach('<div class="fanyi-navigation-bar-wrapper" style="width: 1220px;"><img class="logo" src="https://fanyi-cdn.cdn.bcebos.com/static/translation/img/header/logo_e835568.png"><div class="navigation-wrapper"><div class="normal-navigation"><span class="navigation-text navigation-text-active">文本翻译</span><div class="doc-trans"><div class="upgrade-tag">全新升级</div><span class="navigation-text">文档翻译</span></div><span class="navigation-text">人工翻译</span><span class="navigation-text">视频翻译</span><span class="navigation-text">AI同传</span><span class="navigation-text">翻译API</span><span class="navigation-text">官网</span></div><div class="vip-btn">开通文档翻译VIP</div><div class="user-info-wrapper"><img class="user-avatar" src="http://himg.bdimg.com/sys/portrait/item/translate.1.90fbe9d9.yv0L5WNzFnPsllrw3T0eDw.jpg"><span class="username">爵士舞生活</span><div class="arrow"></div></div></div></div>', name="html展示",
                          attachment_type=allure.attachment_type.HTML)
            print("这是登录测试用例，登录成功")

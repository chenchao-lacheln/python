# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: test_appiumide.py
# @Author: lacheln
# @Time: 12月 06, 2021
# ---

from appium import webdriver
desire_cap = {
  "platformName": "Android",
  "deviceName": "emulator-5554",
  "appPackage": "youqu.android.todesk",
  "appActivity": ".activity.WelcomeActivity"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wb/hub",desire_cap)
el1 = driver.find_element_by_id("youqu.android.todesk:id/tvLogin")
el1.click()
el2 = driver.find_element_by_id("youqu.android.todesk:id/etPhone")
el2.click()
el2.send_keys("17511618501")
el3 = driver.find_element_by_id("youqu.android.todesk:id/btSendCode")
el3.click()
el4 = driver.find_element_by_id("youqu.android.todesk:id/btSendCode")
el4.click()
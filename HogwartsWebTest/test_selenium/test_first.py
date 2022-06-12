# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
#
#
# class TestHogwarts:
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("https://www.baidu.com/")
#         self.driver.implicitly_wait(5)
#
#     def teardown(self):
#         self.driver.quit()
#
#     def test_baidu(self):
#         self.driver.find_element(By.ID,"kw").send_keys("重庆移通学院")
#         self.driver.find_element(By.ID,"su").click()
#         self.driver.find_element(By.LINK_TEXT,'重庆移通学院 - 百度百科')


from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCss():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
    def teardown(self):
        self.driver.quit()
    def test_baidu(self):
        # self.driver.find_element(By.NAME,'wd').send_keys('霍格沃兹测试学院')
        #name属性定位失败百度首页-#wd
        self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('霍格沃兹测试学院')
        # self.driver.find_element(By.XPATH,'//*[@name="wd"]').send_keys('霍格沃兹测试学院')
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()



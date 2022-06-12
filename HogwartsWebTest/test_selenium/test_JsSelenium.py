import time

from test_selenium.base import Base


class TestJs(Base):
    def test_js(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        element_click = self.driver.execute_script('return document.getElementById("su")')
        element_click.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]')
        time.sleep(3)
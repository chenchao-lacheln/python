from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # 打开窗口最大化
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    # 跳过
    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        element_click = self.driver.find_element(By.XPATH,'//*[@value="click me"]')
        element_dbl_click = self.driver.find_element(By.XPATH,'//*[@value="dbl click me"]')
        element_right_click = self.driver.find_element(By.XPATH,'//*[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_dbl_click)
        action.context_click(element_right_click)
        sleep(3)
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_move_to_element(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.CSS_SELECTOR,'#s-usersetting-top')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get('https://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element_by_id('dragger')
        drop_element = self.driver.find_element_by_xpath('/html/body/div[2]')

        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element,drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(3)

    def test_keys(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id('kw').click()
        action = ActionChains(self.driver)
        action.send_keys('chenchao').pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('liushuqi').pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)
    # if __name__ == '__main__':
    #     pytest.main(['-v','-s','test_actionchains.py'])
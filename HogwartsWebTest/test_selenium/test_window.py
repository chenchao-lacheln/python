from test_selenium.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text('登录').click()
        self.driver.find_element_by_link_text('立即注册').click()
        window = self.driver.window_handles
        self.driver.switch_to_window(window[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('18896103409')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('kkkkkkk')
        self.driver.switch_to_window(window[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('18896103409')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('cche62484524')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()

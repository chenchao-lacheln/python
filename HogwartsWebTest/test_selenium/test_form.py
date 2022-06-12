from selenium import webdriver
from time import sleep

class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardowm(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id('user_login').send_keys('1323')
        self.driver.find_element_by_id('user_password').send_keys('sadada')
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[3]/div/label').click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input')
        sleep(3)

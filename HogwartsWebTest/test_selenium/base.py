import os

from selenium import webdriver

class Base():
    def setup(self):
        browser = os.getenv('browser')
        if browser == 'firefox':
            self.driver = webdriver.firefox()
        elif browser == 'headless':
            self.driver == webdriver.phantomjs()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardowm(self):
        self.driver.quit()
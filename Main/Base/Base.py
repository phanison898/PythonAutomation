import time
import pytest
import allure
import os
from allure_commons.types import AttachmentType
from selenium import webdriver


class Base:
    # assigns the name of the browser
    browser_name = "chrome"

    # web site url
    url = "http://www.google.com"

    # set page load time out in seconds
    page_load_time = 30

    # set script load time out
    script_load_time = 10

    # set implicit wait time
    implicit_wait = 10

    # This stores current working directory path
    current_dir = os.getcwd()

    # web driver initialization
    driver = None

    '''
    This method gets invoke automatically before each and every test case
    browser configurations will be configured in this method
    '''

    @pytest.fixture()
    def browser_initialization(self):

        if self.browser_name == "chrome":
            chrome_driver_path = self.current_dir + "/Resources/Drivers/chromedriver.exe"
            self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        elif self.browser_name == "firefox":
            firefox_driver_path = self.current_dir + ""
            self.driver = webdriver.Firefox(executable_path=firefox_driver_path)
        else:
            print("NO_BROWSER_FOUND_EXCEPTION")

        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.set_page_load_timeout(time_to_wait=self.page_load_time)
        self.driver.set_script_timeout(time_to_wait=self.script_load_time)
        self.driver.implicitly_wait(time_to_wait=self.implicit_wait)
        self.driver.get(self.url)

        # following steps execute after every test case
        yield
        self.driver.close()
        self.driver.quit()

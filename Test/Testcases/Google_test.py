from selenium.webdriver.common.keys import Keys
from time import sleep

from Main.Base.Base import Base
import pytest


class GoogleTest(Base):
    '''
    This is a sample test case which
    validates the search box functionality
    of google page
    '''

    def test_google_search_box(self):
        search_box = self.driver.find_element_by_name("q")
        search_box.clear()
        search_box.send_keys("naga phani kumar")
        search_box.send_keys(Keys.ENTER)
        sleep(10)

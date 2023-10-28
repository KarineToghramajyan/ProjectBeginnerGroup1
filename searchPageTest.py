import time
import unittest
from selenium import webdriver
from navigationBar import NavigationBar
from searchResultPage import SearchResult

class SearchProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.apple.com")

    def test_search_product_first(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_search_button()
        navigationBarObj.fill_search_box("airpods")
        time.sleep(5)
        searchResultPageObj = SearchResult(self.driver)
        searchResultPageObj.click_first_result()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()
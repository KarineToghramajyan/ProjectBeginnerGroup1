from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from basePage import BasePage

class SearchResult(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_first_result(self):
        firstResult = self._find_element(By.CSS_SELECTOR, ".rf-serp-explore-image[src='https://www.apple.com/autopush/ww/search/modules/airpods/image__d4v5p0w2oaky_large_2x.jpg?']")
        self._click(firstResult)




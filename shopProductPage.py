from selenium.webdriver.common.by import By
from selenium import webdriver
from basePage import BasePage


class ShopProductPage(BasePage):
    def init(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_to_second_product(self):
        secondProductElement = self._find_element(By.XPATH, "//img[@src='https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/mac-card-40-macbook-air-13-15-202306?wid=1200&hei=1000&fmt=p-jpg&qlt=95&.v=1684262493564']")
        self._click(secondProductElement)
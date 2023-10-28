from selenium.webdriver.common.by import By
from selenium import webdriver
from basePage import BasePage

class StorePage(BasePage):
    def init(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_to_first_product(self):
        firstProductElement = self._find_element(By.XPATH, "//img[@src='https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/store-card-14-16-mac-nav-202301?wid=400&hei=260&fmt=png-alpha&.v=1670959891635']")
        self._click(firstProductElement)
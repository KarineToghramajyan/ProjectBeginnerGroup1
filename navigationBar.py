from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from basePage import BasePage

class NavigationBar(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_search_button(self):
        searchButtonElement = self._find_element(By. ID, "globalnav-menubutton-link-search")
        self._click(searchButtonElement)

    def fill_search_box(self, product):
        searchBoxElement = self._find_element(By.XPATH, "//input[@placeholder='Search apple.com']")
        searchBoxElement.clear()
        self._fill_field(searchBoxElement, product)
        sleep(3)
        searchBoxElement.send_keys(Keys.ENTER)
        sleep(3)

    def click_to_store_button(self):
        storebuttonElement = self._find_element(By.XPATH, "//span[@class='globalnav-link-text-container'][1]")
        self._click(storebuttonElement)




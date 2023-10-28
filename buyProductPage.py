from selenium.webdriver.common.by import By
from basePage import BasePage


class BuyProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_to_buy_button(self, buyButtonElement=None):
        self._find_element(By.XPATH, "(//a[@class='button rf-digitalmat-button'])[1]")
        self._click(buyButtonElement)

    def _find_element(self, XPATH, param):
        pass

    def _click(self, buyButtonElement):
        pass

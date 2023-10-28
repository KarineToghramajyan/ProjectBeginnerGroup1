import unittest
from selenium import webdriver
from navigationBar import NavigationBar
from storePage import StorePage
from shopProductPage import ShopProductPage
from buyProductPage import BuyProductPage
from time import sleep



class BuyProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.get("https://www.apple.com/")

    def test_buy_product(self):
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.click_to_store_button()

        storePageObj = StorePage(self.driver)
        storePageObj.click_to_first_product()

        shopProductPageObj = ShopProductPage(self.driver)
        shopProductPageObj.click_to_second_product()

        buyProductObj = BuyProductPage(self.driver)
        buyProductObj.click_to_buy_button()
        sleep(6)

    def tearDown(self):
        self.driver.close()

from .product_page_locators import ProductPageLocators as Loc
from TestPageObj.pages.base_page import BasePage


class ProductPage(BasePage):
    def add_product(self):
        button = self.browser.find_element(*Loc.add_to_basket_btn)
        button.click()
        self.solve_quiz_and_get_code()

    def check_added_product_name(self):
        product = self.browser.find_element(*Loc.product_name).text
        added_product = self.browser.find_element(*Loc.added_product_name).text
        assert product == added_product, f"Expected {product}, got {added_product}"

    def check_added_product_price(self):
        price = self.browser.find_element(*Loc.product_price).text
        basket_price = self.browser.find_element(*Loc.basket_price).text
        assert price == basket_price, f"Expected {basket_price}, got {basket_price}"

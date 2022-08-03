from selenium.webdriver.common.by import By


class ProductPageLocators:
    added_product_name = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    basket_price = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")
    product_name = (By.CSS_SELECTOR, ".product_main>h1")
    product_price = (By.CSS_SELECTOR, ".product_main>.price_color")
    add_to_basket_btn = (By.CSS_SELECTOR, "#add_to_basket_form>button.btn-add-to-basket")

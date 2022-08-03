from selenium.webdriver.common.by import By


class LoginPageLocators:
    login_form = (By.CSS_SELECTOR, "#login_form")
    register_form = (By.CSS_SELECTOR, "#register_form")

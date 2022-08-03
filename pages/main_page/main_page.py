from TestPageObj.pages.base_page import BasePage
from .main_page_locators import MainPageLocators as Loc
from TestPageObj.pages.login_page.login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*Loc.login_link)
        login_link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*Loc.login_link), "Login link is not presented"

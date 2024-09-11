from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(driver=self.driver, url=self.driver.current_ulr)
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"



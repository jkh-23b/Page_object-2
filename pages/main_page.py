from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
<<<<<<< HEAD
    def go_to_login_page1(self):
        login_link = self.driver.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def go_to_login_link(self):
        login_link = self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"

=======
    def go_to_login_page(self):
        link = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(driver=self.driver, url=self.driver.current_ulr)
>>>>>>> 313f534e26f446fa60415e6be6977a21773c46b0
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        link = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        #return LoginPage(driver=self.driver, url=self.driver.current_url)



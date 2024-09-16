from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def check_product_name_in_basket(self):
        book_name = self.driver.find_element(*ProductPageLocators.BOOK_NAME).text
        name_in_basket = self.driver.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_BASKET).text
        assert book_name == name_in_basket,\
        "Name of choosen on book is not found"

    def check_product_price_in_basket(self):
        book_price = self.driver.find_element(*ProductPageLocators.BOOK_PRICE).text
        price_in_basket = self.driver.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert book_price == price_in_basket, "Price of choosen book is not found"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.NAME_OF_BOOK_IN_BASKET),\
        "Success message is presented, but should not be"

    def should_disapper_button(self):
        assert self.is_disappeared(*ProductPageLocators.NAME_OF_BOOK_IN_BASKET),\
        "Success message is not disappeared"


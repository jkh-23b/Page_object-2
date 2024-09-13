from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.XPATH, "//a[@id='login_link']")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//div[contains(@class, 'register_form')]")

class ProductPageLocators():
    ADD_TO_BASKET = (By.XPATH, "//form[@id='add_to_basket_form']")
    BOOK_NAME = (By.XPATH, "//div[contains(@class, 'product_main')]/h1")
    BOOK_PRICE = (By.XPATH, "//div[contains(@class, 'product_main')]/p[1]")

    NAME_OF_BOOK_IN_BASKET = (By.XPATH, "(//div[@class='alertinner ']//strong)[1]")
    PRICE_IN_BASKET = (By.XPATH, "(//div[@class='alertinner ']//strong)[3]")







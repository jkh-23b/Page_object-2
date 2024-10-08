import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage

@pytest.mark.skip
def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(driver, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()

@pytest.mark.skip
def test_guest_can_go_to_login_page2(driver):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(driver, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()

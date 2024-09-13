import time

import pytest
from pages.product_page import ProductPage
@pytest.mark.skip
def test_guest_can_add_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.solver_quiz_and_get_code()
    page.check_product_name_in_basket()
    page.check_product_price_in_basket()
@pytest.mark.skip
def test_guest_can_add_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.solver_quiz_and_get_code()
    page.check_product_name_in_basket()
    page.check_product_price_in_basket()

@pytest.mark.parametrize('links', ['?promo=offer0',
                                   '?promo=offer1',
                                   '?promo=offer2',
                                   '?promo=offer3',
                                   '?promo=offer4',
                                   '?promo=offer5',
                                   '?promo=offer6',
                                   pytest.param('?promo=offer7', marks=pytest.mark.xfail(
                                       reason="Bug in WIP")
                                   ),
                                   '?promo=offer8',
                                   '?promo=offer9'])
def test_parametrize_links(driver, links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{links}"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.solver_quiz_and_get_code()
    page.check_product_price_in_basket()
    page.check_product_name_in_basket()



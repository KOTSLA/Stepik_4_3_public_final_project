import pytest
import time
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from urls import urls

# @pytest.mark.skip(reason="Test is Ok")
@pytest.mark.parametrize('link', urls)
def test_guest_should_see_login_link_on_product_page(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrize('link', urls)
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.parametrize('link', urls)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_bucket_button()
    page.go_to_bucket_page()
    bucket_page = BasketPage(browser, browser.current_url)
    bucket_page.shuld_be_basket_page()

import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from urls import urls


# @pytest.mark.skip(reason="Test is Ok")
@pytest.mark.parametrize('link', urls)
def test_guest_should_see_login_link_on_product_page(browser,link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# @pytest.mark.skip(reason="Test is Ok")
@pytest.mark.parametrize('link', urls)
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# @pytest.mark.skip(reason="Test is Ok")
@pytest.mark.parametrize('link', urls)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_bucket_button()
    page.go_to_bucket_page()
    bucket_page = BasketPage(browser, browser.current_url)
    bucket_page.shuld_be_basket_page()

# @pytest.mark.skip(reason="Test is Ok")
class TestUserAddToBasketFromProductPage:
    @pytest.mark.parametrize('link', urls)
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_product_page()
        page.solve_quiz_and_get_code()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        emails = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email=emails, password="Stepik123£")
        login_page.should_be_authorized_user()
        login_page.go_to_bucket_page()
        bucket_page = BasketPage(browser, browser.current_url)
        bucket_page.should_not_be_success_message()

    @pytest.mark.parametrize('link', urls)
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_product_page()
        page.solve_quiz_and_get_code()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        emails = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email=emails, password="Stepik123£")
        login_page.should_be_authorized_user()
        login_page.go_to_bucket_page()
        bucket_page = BasketPage(browser, browser.current_url)
        bucket_page.should_not_be_success_message()
        bucket_page.should_be_basket_url()

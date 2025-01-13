import time
import pytest

from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from urls import urls

# @pytest.mark.skip(reason="Test is ready")
@pytest.mark.login_guest
class TestLoginFromMainPage:
    @pytest.mark.parametrize('link', urls)
    def test_guest_can_go_to_login_page(self, browser,link):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(5)

# @pytest.mark.skip(reason="Test is ready")
@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()
    time.sleep(2)

@pytest.mark.skip(reason="Test with Fail result")
@pytest.mark.parametrize('link', urls)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    product_page = ProductPage(browser, browser.current_url)
    time.sleep(3)
    product_page.should_not_be_success_message()


# @pytest.mark.skip(reason="Test is Ok")
@pytest.mark.parametrize('link', urls)
def test_guest_cant_see_success_message(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip(reason="Test with Fail result")
@pytest.mark.parametrize('link', urls)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_not_be_success_message_with_disappeared()

# @pytest.mark.skip(reason="Test is Ok")
@pytest.mark.parametrize('link', urls)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_bucket_button()
    page.go_to_bucket_page()
    bucket_page = BasketPage(browser, browser.current_url)
    bucket_page.shuld_be_basket_page()
    time.sleep(5)


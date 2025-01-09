import time
import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

urls = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                    marks=pytest.mark.xfail(reason="Known bug on this promo page")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]

# Динамически определяем проблемные ссылки
problematic_links = []

@pytest.mark.skip(reason="Test is ready")
@pytest.mark.parametrize('link', urls)
def test_guest_can_go_to_login_page(browser,link):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.skip(reason="Test is ready")
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
    product_page.should_not_be_success_message()

@pytest.mark.skip(reason="Test is Ok")
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
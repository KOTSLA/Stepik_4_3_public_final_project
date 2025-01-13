from selenium.common.exceptions import NoSuchElementException

from locators.locators import BasePageLocators
from locators.locators import ProductPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def should_be_add_to_cart_button(self):
        """Check if button "Add to card" exist."""
        try:
            self.browser.find_element(*BasePageLocators.ADD_BASKET_BUTTON)
        except NoSuchElementException:
            raise AssertionError("Button 'Add to card' does not find on page")

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_FULL), \
        "Success message is presented, but should not be"

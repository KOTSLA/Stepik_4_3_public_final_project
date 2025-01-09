from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators.locators import BucketPageLocators


class BasketPage(BasePage):
    def shuld_be_basket_page(self):
        self.should_bucket_is_empty()
        self.should_be_text_basket_is_empty()

    def should_bucket_is_empty(self):
        # check if button is presented
        assert self.is_not_element_present(*BucketPageLocators.PROCEED_BUTTON), "Button is presented"
        print("Bucket is empty!")

    def should_be_text_basket_is_empty(self):
        text_element = self.browser.find_element(*BucketPageLocators.TEXT_YOU_BASKET_IS_EMPTY)
        text_element_text = text_element.text.strip()
        print(text_element_text)
        assert self.is_element_present(*BucketPageLocators.TEXT_YOU_BASKET_IS_EMPTY), f"Text {text_element_text} is not presented"
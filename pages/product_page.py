from pages.base_page import BasePage

from locators.locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_success_massage_about_include_in_bucket()
        self.item_name_is_similar_selected_item_name()
        self.item_price_is_similar_price_in_bucket()

    # def should_be_login_url(self):
    #     # Check id url is correct
    #     current_url = self.browser.current_url
    #     assert "login" in current_url, f"Expected 'login' to be in URL, but got {current_url}"


    def should_be_success_massage_about_include_in_bucket(self):
        """Check if message 'has been added to your basket.' is enabled."""
        WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE_FULL)
        )
        try:
            self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_FULL)
        except NoSuchElementException:
            raise AssertionError("Item does not add to bucket")

    def item_name_is_similar_selected_item_name(self):
        """Check if message 'has been added to your basket.' is enabled."""
        item_name_element = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_NAME)
        )
        item_name = item_name_element.text.strip()
        print(f"Item name: {item_name}")

        success_message = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE_FULL)
        )
        full_text = success_message.text.strip()

        success_message_strong_element_text = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.SUCCESS_MESSAGE_STRONG)
        )
        strong_text = success_message_strong_element_text.text.strip()
        additional_text = full_text.replace(strong_text, "").strip()
        print(f"Success message: {strong_text} {additional_text}")



        assert item_name == strong_text, (
            f"Item name '{item_name}' is not found in success message '{strong_text}'."
        )

    def item_price_is_similar_price_in_bucket(self):
        item_price = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.PRODUCT_PRICE)
        )
        print(item_price.text)
        bucket_price_message = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(ProductPageLocators.PRICE_BUCKET_MESSAGE)
        )
        print(bucket_price_message.text)
        assert item_price.text in bucket_price_message.text, "Bucket price is not similar selected item price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_FULL), \
        "Success message is presented, but should not be"

    def should_not_be_success_message_with_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_FULL), \
        "Success message is not disappeared"

    #
    # def should_be_register_form(self):
    #     # check if registration form is presented
    #     assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register form is not presented"

from pages.base_page import BasePage

from locators.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Check id url is correct
        current_url = self.browser.current_url
        assert "login" in current_url, f"Expected 'login' to be in URL, but got {current_url}"
        print("Login page is OPEN")

    def should_be_login_form(self):
        # check if login form is presented
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login form is not presented"

    def should_be_register_form(self):
        # check if registration form is presented
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register form is not presented"

    def register_new_user(self, email, password):
        """
        Registration on site.
        """
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_USER_EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_USER_PASSWORD_INPUT)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTER_USER_PASSWORD)
        register_user_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        email_input.clear()
        email_input.send_keys(email)

        password_input.clear()
        password_input.send_keys(password)

        confirm_password_input.clear()
        confirm_password_input.send_keys(password)

        register_user_button.click()
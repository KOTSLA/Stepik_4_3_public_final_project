from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUCKET_BUTTON_LINK = (By.XPATH, "//a[@class='btn btn-default']")

class MainPageLocators:
    ADD_BASKET_BUTTON = (By.XPATH, "//*[@id='add_to_basket_form']/button")

class LoginPageLocators:
    REGISTER_BUTTON = (By.XPATH, "//*[@id='register_form']/button")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='login_form']/button")

class ProductPageLocators:
    SUCCESS_MESSAGE_STRONG = (By.XPATH, "//div[@class='alertinner ']/strong")
    SUCCESS_MESSAGE_FULL = (By.XPATH, "//div[@class='alertinner ']")
    PRODUCT_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRICE_BUCKET_MESSAGE = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]")

class BucketPageLocators:
    PROCEED_BUTTON = (By.XPATH, "//a[@class='btn btn-lg btn-primary btn-block']")
    TEXT_YOU_BASKET_IS_EMPTY = (By.XPATH, "//*[@id='content_inner']/p")
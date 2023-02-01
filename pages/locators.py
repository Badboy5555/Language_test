from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#login_form")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".btn[name='registration_submit']")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_TRUE_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_CART_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner>p")
    PRODUCT_CART_PRICE = (By.CSS_SELECTOR, ".alertinner>p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group>a")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    BASKET_WITH_ITEMS_MESSAGE = (By.CSS_SELECTOR, "#content_inner .row>h2")

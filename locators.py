from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#login_form")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_TRUE_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_CART_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alertinner>p")
    PRODUCT_CART_PRICE = (By.CSS_SELECTOR, ".alertinner>p strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
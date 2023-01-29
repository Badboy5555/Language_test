from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators import ProductPageLocators

class ProductPage(BasePage):
    def add_item_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()
        self.solve_quiz_and_get_code()

    def should_be_a_message(self):
        assert 'был добавлен в вашу корзину' in self.elements_present(*ProductPageLocators.PRODUCT_MESSAGE)[0],"No acception message for item've added to cart"

    def product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_TRUE_NAME).text
        return product_name

    def should_be_true_name_of_the_item(self):
        assert self.product_name() in self.elements_present(*ProductPageLocators.PRODUCT_NAME)[0], "Not a true name of the item"

    def should_be_product_cart_price_message(self):
        assert 'Стоимость корзины теперь составляет' in self.elements_present(*ProductPageLocators.PRODUCT_CART_PRICE_MESSAGE)[0], "No price message for item've added to cart"

    def product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def should_be_true_price_of_the_item(self):
        assert self.product_price() in self.elements_present(*ProductPageLocators.PRODUCT_CART_PRICE)[0], "Not a true price of the item"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_MESSAGE),"Message is present"

    def should_be_hiding_message(self):
        assert not self.is_disappeared(*ProductPageLocators.PRODUCT_MESSAGE), "Element is still present"

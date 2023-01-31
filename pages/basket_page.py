from .base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message_of_empty_basket(self):
        assert 'Ваша корзина пуста' in self.elements_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)[0], "Message is not 'Ваша корзина пуста'"

    def should_be_items_message(self):
        assert 'Товары в корзине' not in self.elements_present(*BasketPageLocators.BASKET_WITH_ITEMS_MESSAGE), 'Basket is not empty'

import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com'
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()

        email = str(time.time()) + "@fakemail.org"
        password = 'dsgfasdgsadfasf'
        self.page.register_new_user(email, password)
        self.page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_cart()
        page.should_be_a_message()
        page.should_be_true_name_of_the_item()
        page.should_be_product_cart_price_message()
        page.should_be_true_price_of_the_item()
        '''__Отрицательные тесты: должны заканчиваться ошибкой__'''
        #page.should_not_be_success_message()
        #page.should_be_hiding_message()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

pattern = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
bad_list = [3]
all_links = [pattern + str(num) if num not in bad_list else
                                 pytest.param(pattern + str(num), marks=pytest.mark.xfail(reason = f'Bad link {num}'))
                                 for num in range(10)]

@pytest.mark.need_review
@pytest.mark.parametrize('link', all_links)
def test_guest_can_add_product_to_basket(browser, link):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_be_a_message()
    page.should_be_true_name_of_the_item()
    page.should_be_product_cart_price_message()
    page.should_be_true_price_of_the_item()
    '''__Отрицательные тесты: должны заканчиваться ошибкой__'''
    #page.should_not_be_success_message()
    #page.should_be_hiding_message()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_be_hiding_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser,link)
    page.should_be_items_message()
    page.should_be_message_of_empty_basket()

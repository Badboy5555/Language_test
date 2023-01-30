from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


def est_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def est_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def est_should_be_login_page(browser):
    link='http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

def est_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com'
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser,link)
    page.should_be_items_message()
    page.should_be_message_of_empty_basket()
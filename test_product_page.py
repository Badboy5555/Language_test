import pytest
from pages.product_page import ProductPage

pattern = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
bad_list = []
all_links = [pattern + str(num) if num not in bad_list else
                                  pytest.param(pattern + str(num), marks=pytest.mark.xfail(reason = f'Bad link {num}'))
                                  for num in range(10)]


@pytest.mark.parametrize('link', all_links)
def test_guest_can_add_product_to_basket(browser, link):
    #link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_cart()
    page.should_be_a_message()
    page.should_be_true_name_of_the_item()
    page.should_be_product_cart_price_message()
    page.should_be_true_price_of_the_item()


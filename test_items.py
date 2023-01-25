import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_page_should_have_goods_button(browser):
    browser.get(link)
    #time.sleep(30)
    assert len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")) >= 1, 'test_page_should_have_goods_button'
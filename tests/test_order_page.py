import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page_locators import HomePageLocators
from pages.order_page import OrderPage


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def test_successful_order_creation(self):
        order_page = OrderPage(self.driver)

        order_page.load()
        order_page.pass_first_step()
        order_page.pass_second_step()
        order_page.confirm_order()

        assert order_page.is_order_confirmed() is True

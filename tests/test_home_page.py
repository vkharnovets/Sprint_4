import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators


class TestHomePage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @pytest.mark.parametrize('question_locator, answer_locator', [(HomePageLocators.question_1_heading, HomePageLocators.question_1_answer),
                                                                  (HomePageLocators.question_2_heading, HomePageLocators.question_2_answer),
                                                                  (HomePageLocators.question_3_heading, HomePageLocators.question_3_answer),
                                                                  (HomePageLocators.question_4_heading, HomePageLocators.question_4_answer),
                                                                  (HomePageLocators.question_5_heading, HomePageLocators.question_5_answer),
                                                                  (HomePageLocators.question_6_heading, HomePageLocators.question_6_answer),
                                                                  (HomePageLocators.question_7_heading, HomePageLocators.question_7_answer),
                                                                  (HomePageLocators.question_8_heading, HomePageLocators.question_8_answer)])
    def test_correct_answer_is_shown_on_question_click(self, question_locator, answer_locator):
        home_page = HomePage(self.driver)
        home_page.load()

        home_page.click_question(question_locator)
        is_answer_visible = home_page.is_answer_visible(answer_locator)

        assert is_answer_visible is True

    def test_top_order_button_click_navigates_on_orders_page(self):
        home_page = HomePage(self.driver)
        home_page.load()

        home_page.click_top_order_button()

        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(HomePage.url))
        assert self.driver.current_url == OrderPage.url

    def test_bottom_order_button_click_navigates_on_orders_page(self):
        home_page = HomePage(self.driver)
        home_page.load()

        home_page.click_bottom_order_button()

        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(HomePage.url))
        assert self.driver.current_url == OrderPage.url

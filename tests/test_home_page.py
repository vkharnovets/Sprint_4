import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators


class TestHomePage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    @allure.description('Нажимаем на стрелочку рядом с вопросом и проверяем, что открывается соответствующий текст')
    @pytest.mark.parametrize('question_description, question_locator, answer_locator', [('Вопрос #1 из списка', HomePageLocators.question_1_heading, HomePageLocators.question_1_answer),
                                                                  ('Вопрос #2 из списка', HomePageLocators.question_2_heading, HomePageLocators.question_2_answer),
                                                                  ('Вопрос #3 из списка', HomePageLocators.question_3_heading, HomePageLocators.question_3_answer),
                                                                  ('Вопрос #4 из списка', HomePageLocators.question_4_heading, HomePageLocators.question_4_answer),
                                                                  ('Вопрос #5 из списка', HomePageLocators.question_5_heading, HomePageLocators.question_5_answer),
                                                                  ('Вопрос #6 из списка', HomePageLocators.question_6_heading, HomePageLocators.question_6_answer),
                                                                  ('Вопрос #7 из списка', HomePageLocators.question_7_heading, HomePageLocators.question_7_answer),
                                                                  ('Вопрос #8 из списка', HomePageLocators.question_8_heading, HomePageLocators.question_8_answer)])
    def test_correct_answer_is_shown_on_question_click(self, question_description, question_locator, answer_locator):
        home_page = HomePage(self.driver)
        home_page.load()

        home_page.click_question(question_locator, question_description)
        is_answer_visible = home_page.is_answer_visible(answer_locator)

        assert is_answer_visible is True

    def test_top_order_button_click_navigates_on_orders_page(self):
        home_page = HomePage(self.driver)
        home_page.load()

        home_page.click_top_order_button()

        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(Urls.home_page))
        assert self.driver.current_url == Urls.order_page

    def test_bottom_order_button_click_navigates_on_orders_page(self):
        home_page = HomePage(self.driver)
        home_page.load()

        home_page.click_bottom_order_button()

        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(Urls.home_page))
        assert self.driver.current_url == Urls.order_page

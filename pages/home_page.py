import allure
from urls import Urls
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем на верхнюю кнопку \'Заказать\'')
    def click_top_order_button(self):
        self.click_element(HomePageLocators.TOP_ORDER_BUTTON)

    @allure.step('Кликаем на нижнюю кнопку \'Заказать\'')
    def click_bottom_order_button(self):
        self.click_element(HomePageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step('Кликаем на {question}, используя локатор {question_locator}')
    def click_question(self, question_locator, question):
        self.click_element(question_locator)

    @allure.step('Проверяем, что показался правильный ответ, используя локатор {answer_locator}')
    def is_answer_visible(self, answer_locator):
        return self.get_element(answer_locator).get_attribute('hidden') is None

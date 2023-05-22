import allure
from urls import Urls
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, Urls.home_page)

    @allure.step('Кликаем на верхнюю кнопку \'Заказать\'')
    def click_top_order_button(self):
        self.driver.find_element(*HomePageLocators.top_order_button).click()

    @allure.step('Кликаем на нижнюю кнопку \'Заказать\'')
    def click_bottom_order_button(self):
        self.driver.find_element(*HomePageLocators.bottom_order_button).click()

    @allure.step('Кликаем на {question_description}, используя локатор {question_locator}')
    def click_question(self, question_locator, question_description):
        self.driver.find_element(*question_locator).click()

    @allure.step('Проверяем, что показался правильный ответ, используя локатор {answer_locator}')
    def is_answer_visible(self, answer_locator):
        return self.driver.find_element(*answer_locator).get_attribute('hidden') is None

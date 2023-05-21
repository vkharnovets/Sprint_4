from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://qa-scooter.praktikum-services.ru/')

    def click_top_order_button(self):
        self.driver.find_element(*HomePageLocators.top_order_button).click()

    def click_bottom_order_button(self):
        self.driver.find_element(*HomePageLocators.bottom_order_button).click()

    def click_question(self, question_locator):
        self.driver.find_element(*question_locator).click()

    def is_answer_visible(self, answer_locator):
        return self.driver.find_element(*answer_locator).get_attribute('hidden') is None

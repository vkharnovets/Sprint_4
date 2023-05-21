from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from urls import Urls
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, Urls.order_page)

    def choose_metro(self):
        self.driver.find_element(*OrderPageLocators.metro_combobox).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.metro_value))
        self.driver.find_element(*OrderPageLocators.metro_value).click()

    def pass_first_step(self, order_data):
        self.driver.find_element(*OrderPageLocators.name_textbox).send_keys(order_data['name'])
        self.driver.find_element(*OrderPageLocators.family_name_textbox).send_keys(order_data['family_name'])
        self.driver.find_element(*OrderPageLocators.address_textbox).send_keys(order_data['address'])
        self.choose_metro()
        self.driver.find_element(*OrderPageLocators.phone_textbox).send_keys(order_data['phone'])

        self.driver.find_element(*OrderPageLocators.next_button).click()

    def choose_date(self):
        self.driver.find_element(*OrderPageLocators.calendar_control).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.calendar_value))
        self.driver.find_element(*OrderPageLocators.calendar_value).click()

    def choose_period(self):
        self.driver.find_element(*OrderPageLocators.period_combobox).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.period_value))
        self.driver.find_element(*OrderPageLocators.period_value).click()

    def pass_second_step(self, order_data):
        self.choose_date()
        self.choose_period()
        self.driver.find_element(*OrderPageLocators.black_color_checkbox).click()
        self.driver.find_element(*OrderPageLocators.comment_textbox).send_keys(order_data['comment'])
        self.driver.find_element(*OrderPageLocators.order_button).click()

    def confirm_order(self):
        self.driver.find_element(*OrderPageLocators.confirm_order_button).click()

    def is_order_confirmed(self):
        return len(self.driver.find_elements(*OrderPageLocators.order_confirmation)) > 0

    def click_scooter_link(self):
        self.driver.find_element(*OrderPageLocators.scooter_page_link).click()

    def click_yandex_link(self):
        self.driver.find_element(*OrderPageLocators.yandex_page_link).click()



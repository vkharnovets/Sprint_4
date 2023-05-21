from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, 'https://qa-scooter.praktikum-services.ru/order')

    def choose_metro(self):
        self.driver.find_element(*OrderPageLocators.metro_combobox).click()
        self.driver.find_element(*OrderPageLocators.metro_value).click()

    def pass_first_step(self):
        self.driver.find_element(*OrderPageLocators.name_textbox).send_keys('Виктория')
        self.driver.find_element(*OrderPageLocators.family_name_textbox).send_keys('Харновец')
        self.driver.find_element(*OrderPageLocators.address_textbox).send_keys('Ленина 12-1-34')
        self.choose_metro()
        self.driver.find_element(*OrderPageLocators.phone_textbox).send_keys('+79061234567')

        self.driver.find_element(*OrderPageLocators.next_button).click()

    def choose_date(self):
        self.driver.find_element(*OrderPageLocators.calendar_control).click()
        self.driver.find_element(*OrderPageLocators.calendar_value).click()

    def choose_period(self):
        self.driver.find_element(*OrderPageLocators.period_combobox).click()
        self.driver.find_element(*OrderPageLocators.period_value).click()

    def pass_second_step(self):
        self.choose_date()
        self.choose_period()
        self.driver.find_element(*OrderPageLocators.black_color_checkbox).click()
        self.driver.find_element(*OrderPageLocators.comment_textbox).send_keys('Заберу у подъезда')
        self.driver.find_element(*OrderPageLocators.order_button).click()

    def confirm_order(self):
        self.driver.find_element(*OrderPageLocators.confirm_order_button).click()

    def is_order_confirmed(self):
        return len(self.driver.find_elements(*OrderPageLocators.order_confirmation)) > 0



import allure
from urls import Urls
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        super().load(Urls.order_page)

    @allure.step('Выбираем станцию метро')
    def choose_metro(self):
        self.click_element(OrderPageLocators.METRO_COMBOBOX)
        self.wait_element(OrderPageLocators.METRO_VALUE)
        self.click_element(OrderPageLocators.METRO_VALUE)

    @allure.step('Проходим первый экран визарда')
    def pass_first_step(self, order_data):
        self.enter_text(OrderPageLocators.NAME_TEXTBOX, order_data['name'])
        self.enter_text(OrderPageLocators.FAMILY_NAME_TEXTBOX, order_data['family_name'])
        self.enter_text(OrderPageLocators.ADDRESS_TEXTBOX, order_data['address'])
        self.choose_metro()
        self.enter_text(OrderPageLocators.PHONE_TEXTBOX, order_data['phone'])

        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Выбираем дату')
    def choose_date(self):
        self.click_element(OrderPageLocators.CALENDAR_CONTROL)
        self.wait_element(OrderPageLocators.CALENDAR_VALUE)
        self.click_element(OrderPageLocators.CALENDAR_VALUE)

    @allure.step('Выбираем срок аренжы')
    def choose_period(self):
        self.click_element(OrderPageLocators.PERIOD_COMBOBOX)
        self.wait_element(OrderPageLocators.PERIOD_VALUE)
        self.click_element(OrderPageLocators.PERIOD_VALUE)

    @allure.step('Проходим второй экран визарда')
    def pass_second_step(self, order_data):
        self.choose_date()
        self.choose_period()
        self.click_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        self.enter_text(OrderPageLocators.COMMENT_TEXTBOX, order_data['comment'])
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Жмем кнопку подтверждения заказа')
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step('Проверяем, что заказ подтвержден')
    def is_order_confirmed(self):
        return self.has_element(OrderPageLocators.ORDER_CONFIRMATION)

    @allure.step('Кликаем на лого \'Самокат\'')
    def click_scooter_link(self):
        self.click_element(OrderPageLocators.SCOOTER_PAGE_LINK)

    @allure.step('Кликаем на лого \'Яндекс\'')
    def click_yandex_link(self):
        self.click_element(OrderPageLocators.YANDEX_PAGE_LINK)



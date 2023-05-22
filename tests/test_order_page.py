import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from pages.order_page import OrderPage


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('Проверка позитивного сценария размещения заказа')
    @allure.description('Проходим визард размещения заказа по шагам, используя тестовые данные из параметров теста')
    @pytest.mark.parametrize('order_data', [
        {
            'name': 'Виктория',
            'family_name': 'Харновец',
            'address': 'Ленина 12-1-34',
            'phone': '+79061234567',
            'comment': 'Заберу у подъезда'
        },
        {
            'name': 'Василий',
            'family_name': 'Пупкин',
            'address': 'Комсомола 11-2-65',
            'phone': '+79261234567',
            'comment': 'Встретит бабушка'
        }])
    def test_successful_order_creation(self, order_data):
        order_page = OrderPage(self.driver)

        order_page.load()
        order_page.pass_first_step(order_data)
        order_page.pass_second_step(order_data)
        order_page.confirm_order()

        assert order_page.is_order_confirmed() is True

    @allure.title('Проверка перехода на Яндекс.Дзен по ссылке')
    @allure.description('Кликаем по логотипу Яндекс и ожидаем, что в новом окне откроется Яндекс.Дзен')
    def test_yandex_link_click_navigates_on_dzen_in_new_tab(self):
        order_page = OrderPage(self.driver)
        order_page.load()

        order_page.click_yandex_link()

        browser_tabs = self.driver.window_handles
        self.driver.switch_to.window(browser_tabs[1])

        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(Urls.dzen_page))
        assert self.driver.current_url == Urls.dzen_page

    @allure.title('Проверка перехода на главную страницу при нажатии на логотип \'Самокат\'')
    @allure.description('Кликаем по логотипу \'Самокат\' и ожидаем, что откроется главная страница приложения')
    def test_scooter_link_click_navigates_on_home_page(self):
        order_page = OrderPage(self.driver)
        order_page.load()

        order_page.click_scooter_link()

        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(Urls.order_page))
        assert self.driver.current_url == Urls.home_page

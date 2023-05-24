import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from urls import Urls
from test_data.orders import Orders
from pages.order_page import OrderPage
from pages.home_page import HomePage
from locators.dzen_page_locators import DzenPageLocators

class TestOrderPage:
    @allure.title('Проверка позитивного сценария размещения заказа')
    @allure.description('Проходим визард размещения заказа по шагам, используя тестовые данные из параметров теста')
    @pytest.mark.parametrize('order_data', [Orders.order_for_vika, Orders.order_for_vasya])
    def test_successful_order_creation(self, driver, order_data):
        order_page = OrderPage(driver)

        order_page.load()
        order_page.pass_first_step(order_data)
        order_page.pass_second_step(order_data)
        order_page.confirm_order()

        assert order_page.is_order_confirmed() is True

    @allure.title('Проверка перехода на Яндекс.Дзен по ссылке')
    @allure.description('Кликаем по логотипу Яндекс и ожидаем, что в новом окне откроется Яндекс.Дзен')
    def test_yandex_link_click_navigates_on_dzen_in_new_tab(self, driver):
        order_page = OrderPage(driver)
        order_page.load()

        order_page.click_yandex_link()

        browser_tabs = driver.window_handles
        driver.switch_to.window(browser_tabs[1])

        order_page.wait_url_changed_to(Urls.dzen_page)
        WebDriverWait(driver, order_page.MAXIMUM_WAIT_TIME_SECS).until(
            expected_conditions.visibility_of_element_located(DzenPageLocators.FIND_BUTTON))

        assert driver.current_url == Urls.dzen_page

    @allure.title('Проверка перехода на главную страницу при нажатии на логотип \'Самокат\'')
    @allure.description('Кликаем по логотипу \'Самокат\' и ожидаем, что откроется главная страница приложения')
    def test_scooter_link_click_navigates_on_home_page(self, driver):
        order_page = OrderPage(driver)
        order_page.load()

        order_page.click_scooter_link()
        order_page.wait_url_changed_to(Urls.home_page)

        home_page = HomePage(driver)
        home_page.wait_page_is_loaded()
        assert home_page.get_url() == Urls.home_page

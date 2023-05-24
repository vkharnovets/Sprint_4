import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    MAXIMUM_WAIT_TIME_SECS = 30

    def __init__(self, driver):
        self.driver = driver

    def get_url(self):
        return self.driver.current_url

    def has_element(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.get_element(locator).click()

    def enter_text(self, locator, text):
        self.get_element(locator).send_keys(text)

    def wait_element(self, locator):
        WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME_SECS).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_url_changed_to(self, new_url):
        WebDriverWait(self.driver, self.MAXIMUM_WAIT_TIME_SECS).until(expected_conditions.url_to_be(new_url))

    @allure.step('Ждем, пока на странице появится лого \'Самокат\'')
    def wait_page_is_loaded(self):
        self.wait_element(BasePageLocators.HOME_PAGE_CONTROL)

    @allure.step('Жмем кнопку согласия на Cookies, если она появилась')
    def accept_cookies(self):
        if self.has_element(BasePageLocators.ACCEPT_COOKIES_BUTTON):
            self.click_element(BasePageLocators.ACCEPT_COOKIES_BUTTON)

    @allure.step('Загружаем страницу')
    def load(self, url):
        self.driver.get(url)
        self.wait_page_is_loaded()
        self.accept_cookies()

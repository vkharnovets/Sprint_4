from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def wait_page_is_loaded(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(BasePageLocators.home_page_link))

    def accept_cookies(self):
        accept_cookies_button = self.driver.find_elements(*BasePageLocators.accept_cookies_button)
        if len(accept_cookies_button) > 0:
            accept_cookies_button[0].click()

    def load(self):
        self.driver.get(self.url)
        self.wait_page_is_loaded()
        self.accept_cookies()


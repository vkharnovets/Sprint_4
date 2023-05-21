from selenium.webdriver.common.by import By


class BasePageLocators:
    home_page_link = [By.XPATH, './/a[@href=\'/\']']
    accept_cookies_button = [By.ID, 'rcc-confirm-button']

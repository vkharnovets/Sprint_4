from selenium.webdriver.common.by import By


class BasePageLocators:
    HOME_PAGE_CONTROL = [By.XPATH, './/a[@href=\'/\']']
    ACCEPT_COOKIES_BUTTON = [By.ID, 'rcc-confirm-button']

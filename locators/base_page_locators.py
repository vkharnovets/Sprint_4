from selenium.webdriver.common.by import By


class BasePageLocators:
    STATUS_BUTTON = [By.XPATH, '(.//button[text()=\'Статус заказа\'])']
    ACCEPT_COOKIES_BUTTON = [By.ID, 'rcc-confirm-button']

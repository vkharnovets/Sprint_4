from selenium.webdriver.common.by import By

class OrderPageLocators:
    YANDEX_PAGE_LINK = [By.XPATH, './/a[@href=\'//yandex.ru\']']
    SCOOTER_PAGE_LINK = [By.XPATH, './/a[@href=\'/\']']

    NAME_TEXTBOX = [By.XPATH, './/input[@placeholder=\'* Имя\']']
    FAMILY_NAME_TEXTBOX = [By.XPATH, './/input[@placeholder=\'* Фамилия\']']
    ADDRESS_TEXTBOX = [By.XPATH, './/input[@placeholder=\'* Адрес: куда привезти заказ\']']
    METRO_COMBOBOX = [By.XPATH, './/input[@placeholder=\'* Станция метро\']']
    METRO_VALUE = [By.XPATH, './/div[text()=\'Черкизовская\']']
    PHONE_TEXTBOX = [By.XPATH, './/input[@placeholder=\'* Телефон: на него позвонит курьер\']']
    NEXT_BUTTON = [By.XPATH, '(.//button[text()=\'Далее\'])']

    CALENDAR_CONTROL = [By.XPATH, './/input[@placeholder=\'* Когда привезти самокат\']']
    #last day on current month daypicker guarantees that selected date is not in the past
    CALENDAR_VALUE = [By.XPATH, './/div[@class=\'react-datepicker__month\']/div[@class=\'react-datepicker__week\'][last()]/div[last()]']
    PERIOD_COMBOBOX = [By.XPATH, './/div[text()=\'* Срок аренды\']']
    PERIOD_VALUE = [By.XPATH, './/div[text()=\'сутки\']']
    BLACK_COLOR_CHECKBOX = [By.XPATH, './/input[@id=\'black\' and @type=\'checkbox\']']
    COMMENT_TEXTBOX = [By.XPATH, './/input[@placeholder=\'Комментарий для курьера\']']
    ORDER_BUTTON = [By.XPATH, '(.//button[text()=\'Заказать\'])[2]']

    CONFIRM_ORDER_BUTTON = [By.XPATH, './/div[text()=\'Хотите оформить заказ?\']/following-sibling::div/button[text()=\'Да\']']
    ORDER_CONFIRMATION = [By.XPATH, './/div[contains(text(),\'Заказ оформлен\')]']





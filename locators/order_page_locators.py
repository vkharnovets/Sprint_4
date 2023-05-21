from selenium.webdriver.common.by import By

class OrderPageLocators:
    yandex_page_link = [By.XPATH, './/a[@href=\'//yandex.ru\']']
    scooter_page_link = [By.XPATH, './/a[@href=\'/\']']

    name_textbox = [By.XPATH, './/input[@placeholder=\'* Имя\']']
    family_name_textbox = [By.XPATH, './/input[@placeholder=\'* Фамилия\']']
    address_textbox = [By.XPATH, './/input[@placeholder=\'* Адрес: куда привезти заказ\']']
    metro_combobox = [By.XPATH, './/input[@placeholder=\'* Станция метро\']']
    metro_value = [By.XPATH, './/div[text()=\'Черкизовская\']']
    phone_textbox = [By.XPATH, './/input[@placeholder=\'* Телефон: на него позвонит курьер\']']
    next_button = [By.XPATH, '(.//button[text()=\'Далее\'])']

    calendar_control = [By.XPATH, './/input[@placeholder=\'* Когда привезти самокат\']']
    #last day on current month daypicker guarantees that selected date is not in the past
    calendar_value = [By.XPATH, './/div[@class=\'react-datepicker__month\']/div[@class=\'react-datepicker__week\'][last()]/div[last()]']
    period_combobox = [By.XPATH, './/div[text()=\'* Срок аренды\']']
    period_value = [By.XPATH, './/div[text()=\'сутки\']']
    black_color_checkbox = [By.XPATH, './/input[@id=\'black\' and @type=\'checkbox\']']
    comment_textbox = [By.XPATH, './/input[@placeholder=\'Комментарий для курьера\']']
    order_button = [By.XPATH, '(.//button[text()=\'Заказать\'])[2]']

    confirm_order_button = [By.XPATH, './/div[text()=\'Хотите оформить заказ?\']/following-sibling::div/button[text()=\'Да\']']
    order_confirmation = [By.XPATH, './/div[contains(text(),\'Заказ оформлен\')]']





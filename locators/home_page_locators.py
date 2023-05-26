from selenium.webdriver.common.by import By


class HomePageLocators:
    TOP_ORDER_BUTTON = [By.XPATH, '(.//button[text()=\'Заказать\'])[1]']
    BOTTOM_ORDER_BUTTON = [By.XPATH, '(.//button[text()=\'Заказать\'])[2]']

    QUESTION_1_HEADING = [By.ID, 'accordion__heading-0']
    QUESTION_1_ANSWER = [By.ID, 'accordion__panel-0']

    QUESTION_2_HEADING = [By.ID, 'accordion__heading-1']
    QUESTION_2_ANSWER = [By.ID, 'accordion__panel-1']

    QUESTION_3_HEADING = [By.ID, 'accordion__heading-2']
    QUESTION_3_ANSWER = [By.ID, 'accordion__panel-2']

    QUESTION_4_HEADING = [By.ID, 'accordion__heading-3']
    QUESTION_4_ANSWER = [By.ID, 'accordion__panel-3']

    QUESTION_5_HEADING = [By.ID, 'accordion__heading-4']
    QUESTION_5_ANSWER = [By.ID, 'accordion__panel-4']

    QUESTION_6_HEADING = [By.ID, 'accordion__heading-5']
    QUESTION_6_ANSWER = [By.ID, 'accordion__panel-5']

    QUESTION_7_HEADING = [By.ID, 'accordion__heading-6']
    QUESTION_7_ANSWER = [By.ID, 'accordion__panel-6']

    QUESTION_8_HEADING = [By.ID, 'accordion__heading-7']
    QUESTION_8_ANSWER = [By.ID, 'accordion__panel-7']

from selenium.webdriver.common.by import By


class HomePageLocators:
    top_order_button = [By.XPATH, '(.//button[text()=\'Заказать\'])[1]']
    bottom_order_button = [By.XPATH, '(.//button[text()=\'Заказать\'])[2]']

    question_1_heading = [By.ID, 'accordion__heading-0']
    question_1_answer = [By.ID, 'accordion__panel-0']

    question_2_heading = [By.ID, 'accordion__heading-1']
    question_2_answer = [By.ID, 'accordion__panel-1']

    question_3_heading = [By.ID, 'accordion__heading-2']
    question_3_answer = [By.ID, 'accordion__panel-2']

    question_4_heading = [By.ID, 'accordion__heading-3']
    question_4_answer = [By.ID, 'accordion__panel-3']

    question_5_heading = [By.ID, 'accordion__heading-4']
    question_5_answer = [By.ID, 'accordion__panel-4']

    question_6_heading = [By.ID, 'accordion__heading-5']
    question_6_answer = [By.ID, 'accordion__panel-5']

    question_7_heading = [By.ID, 'accordion__heading-6']
    question_7_answer = [By.ID, 'accordion__panel-6']

    question_8_heading = [By.ID, 'accordion__heading-7']
    question_8_answer = [By.ID, 'accordion__panel-7']

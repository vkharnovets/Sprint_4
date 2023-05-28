import pytest
import allure
from urls import Urls
from pages.home_page import HomePage
from pages.order_page import OrderPage
from test_data.questions import Questions


class TestHomePage:
    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    @allure.description('Нажимаем на стрелочку рядом с вопросом и проверяем, что открывается соответствующий текст')
    @pytest.mark.parametrize('question', [Questions.question1,
                                          Questions.question2,
                                          Questions.question3,
                                          Questions.question4,
                                          Questions.question5,
                                          Questions.question6,
                                          Questions.question7,
                                          Questions.question8])
    def test_correct_answer_is_shown_on_question_click(self, driver, question):
        home_page = HomePage(driver)

        home_page.click_question(question['locator'], question['text'])
        home_page.wait_element(question['answer_locator'])
        is_answer_visible = home_page.is_answer_visible(question['answer_locator'])
        answer_text = home_page.get_element(question['answer_locator']).text

        assert is_answer_visible is True and answer_text == question['answer']

    @allure.title('Проверка кнопки "Заказать" вверху страницы')
    @allure.description('Нажимаем на кнопки "Заказать" вверху страницы и проверяем, что произошел переход на страницу с заказами')
    def test_top_order_button_click_navigates_on_orders_page(self, driver):
        home_page = HomePage(driver)

        home_page.click_top_order_button()
        home_page.wait_url_changed_to(Urls.order_page)

        order_page = OrderPage(driver)
        order_page.wait_page_is_loaded()
        assert order_page.get_url() == Urls.order_page

    @allure.title('Проверка кнопки "Заказать" внизу страницы')
    @allure.description('Нажимаем на кнопки "Заказать" внизу страницы и проверяем, что произошел переход на страницу с заказами')
    def test_bottom_order_button_click_navigates_on_orders_page(self, driver):
        home_page = HomePage(driver)

        home_page.click_bottom_order_button()
        home_page.wait_url_changed_to(Urls.order_page)

        order_page = OrderPage(driver)
        order_page.wait_page_is_loaded()
        assert order_page.get_url() == Urls.order_page

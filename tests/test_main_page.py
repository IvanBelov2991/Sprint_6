from pages.main_page import MainPage
import pytest
import allure
from data import Urls
from data import QuestionsData


class TestLogoOnMainPage:
    @allure.title('Проверка, что по клику на лого "Самокат" открывается главная страница')
    @allure.description('Заходим на страницу заказа и по клику на лого "Самокат"'
                        ' возвращаемся на главную страницу, проверяем что находимся на главной странице')
    def test_click_on_logo_samokat_return_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)

        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.accept_cookies_button_click()
        main_page.click_header_order_button()
        main_page.wait_for_load_page(Urls.ORDER_PAGE)
        main_page.click_on_logo_samokat()
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.assert_current_page(Urls.MAIN_PAGE)
        assert main_page.wait_for_load_main_page_text() == 'Привезём его прямо к вашей двери,\nа когда накатаетесь — ' \
                                                           'заберём'

    @allure.title('Проверка, что по клику на лого "Яндекс" происходит редирект на Дзен')
    @allure.description('На главной странице кликаем на лого "Яндекс" и проверяем, что находимся на странице Дзена')
    def test_click_on_logo_yandex_redirect_to_dzen_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.accept_cookies_button_click()
        main_page.click_on_logo_yandex()
        main_page.switch_to_page(Urls.DZEN_PAGE)
        main_page.wait_for_load_page(Urls.DZEN_PAGE)
        main_page.assert_current_page(Urls.DZEN_PAGE)


class TestQuestions:

    @pytest.mark.parametrize("question_number, expected_answer", QuestionsData.test_data)
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на вопросы открываются соответствующие тексты')
    def test_questions_on_main_page(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.accept_cookies_button_click()
        main_page.scroll_to_questions_text_header()
        main_page.click_question(question_number)
        main_page.verify_accordion_answer(question_number, expected_answer)


class TestOrderButtons:

    @allure.title('Проверка верхней кнопки "Заказать" на главной странице')
    def test_header_button_on_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.accept_cookies_button_click()
        main_page.click_header_order_button()
        main_page.wait_for_load_page(Urls.ORDER_PAGE)

    @allure.title('Проверка кнопки "Заказать" находящейся на середине страницы')
    def test_middle_button_on_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_load_page(Urls.MAIN_PAGE)
        main_page.accept_cookies_button_click()
        main_page.scroll_to_middle_order_button()
        main_page.click_middle_order_button()
        main_page.wait_for_load_page(Urls.ORDER_PAGE)

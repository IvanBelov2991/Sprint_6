from pages.order_scooter_page import OrderScooterPage
from pages.main_page import MainPage
import pytest
import allure


class TestLogoOnMainPage:
    @allure.title('Проверка, что по клику на лого "Самокат" открывается главная страница')
    @allure.description('Заходим на страницу заказа и по клику на лого "Самокат"'
                        ' возвращаемся на главную страницу, проверяем что находимся на главной странице')
    def test_click_on_logo_samokat_return_to_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderScooterPage(driver)
        main_page.wait_for_load_main_page()
        main_page.accept_cookies_button_click()
        main_page.click_header_order_button()
        order_page.wait_for_order_page_personal_info_header()
        main_page.click_on_logo_samokat()
        main_page.wait_for_load_main_page()

    @allure.title('Проверка, что по клику на лого "Яндекс" происходит редирект на Дзен')
    @allure.description('На главной странице кликаем на лого "Яндекс" и проверяем, что находимся на странице Дзена')
    def test_click_on_logo_yandex_redirect_to_dzen_page(self, driver):
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.accept_cookies_button_click()
        main_page.click_on_logo_yandex()
        main_page.switch_to_page('https://dzen.ru/?yredirect=true')
        main_page.wait_for_redirect_page()


class TestQuestions:

    @pytest.mark.parametrize("question_number, expected_answer", [
        (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (1,
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать '
         'несколько заказов — один за другим.'),
        (2,
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды '
         'начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, '
         'суточная аренда закончится 9 мая в 20:30.'),
        (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (5,
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без '
         'передышек и во сне. Зарядка не понадобится.'),
        (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на вопросы открываются соответствующие тексты')
    def test_questions_on_main_page(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.wait_for_load_main_page()
        main_page.accept_cookies_button_click()
        main_page.scroll_to_questions_text_header()
        main_page.click_question(question_number)
        main_page.verify_accordion_answer(question_number, expected_answer)

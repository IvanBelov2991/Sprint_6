from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class MainPage(BasePage):
    HEADER_ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    MAIN_PAGE_TEXT = (By.XPATH, '//div[@class="Home_SubHeader__zwi_E"]')
    MIDDLE_ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    LOGO_YANDEX = (By.XPATH, '//a[@href="//yandex.ru" and @class="Header_LogoYandex__3TSOI"]/img')
    LOGO_SAMOKAT = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]/img[@alt="Scooter"]')
    QUESTIONS_TEXT_HEADER = (By.XPATH, '//div[@data-accordion-component="Accordion" and contains(@class, "accordion")]')

    @allure.step('Ожидается открытие новой страницы')
    @allure.description('Проверка нахождения на странице по тексту')
    def wait_for_load_main_page_text(self):
        text_on_main_page = self.wait_and_find_element(self.MAIN_PAGE_TEXT)
        return text_on_main_page.text

    @allure.step('Кликаем на верхнюю кнопку "Заказать"')
    def click_header_order_button(self):
        self.click_element(self.HEADER_ORDER_BUTTON)

    @allure.step('Скролл до кнопки в середине страницы "Заказать"')
    def scroll_to_middle_order_button(self):
        self.scroll_to_element(self.MIDDLE_ORDER_BUTTON)
        self.wait_and_find_element(self.MIDDLE_ORDER_BUTTON)

    @allure.step('Клик по кнопке в середине страницы "Заказать"')
    def click_middle_order_button(self):
        self.click_element(self.MIDDLE_ORDER_BUTTON)

    @allure.step('Клик на логотип "Яндекс"')
    def click_on_logo_yandex(self):
        self.click_element(self.LOGO_YANDEX)

    @allure.step('Клик на логотип "Самокат"')
    def click_on_logo_samokat(self):
        self.click_element(self.LOGO_SAMOKAT)

    @allure.step('Скролл до раздела "Вопросы о важном"')
    def scroll_to_questions_text_header(self):
        self.scroll_to_element(self.QUESTIONS_TEXT_HEADER)

    @allure.step('Клик по вопросу по номеру вопроса"')
    def click_question(self, question_number):
        locator = (By.XPATH,
                   f'//div[starts-with(@id, "accordion__heading-{question_number}")'
                   f' and contains(@class, "accordion__button")]')
        self.click_element(locator)

    @allure.step('Проверяем правильность ответа на вопрос по номеру вопроса"')
    def verify_accordion_answer(self, question_number, expected_answer):
        locator = (By.XPATH, f'//div[@id="accordion__panel-{question_number}"]')
        answer_element = self.wait_and_find_element(locator)
        actual_answer = answer_element.text
        assert actual_answer == expected_answer, f"Ожидаемый ответ '{expected_answer}', но найден '{actual_answer}'" \
                                                 f" для вопроса {question_number}"

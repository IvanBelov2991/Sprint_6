import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class MainPage:
    header_order_button = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    main_page_text = (By.XPATH, '//div[@class="Home_SubHeader__zwi_E"]')
    middle_order_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    logo_yandex = (By.XPATH, '//a[@href="//yandex.ru" and @class="Header_LogoYandex__3TSOI"]/img')
    logo_samokat = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]/img[@alt="Scooter"]')
    accept_cookies_button = (By.XPATH, "//button[@id='rcc-confirm-button' and text()='да все привыкли']")
    questions_text_header = (By.XPATH, '//div[@data-accordion-component="Accordion" and contains(@class, "accordion")]')

    def __init__(self, driver):
        self.driver = driver
        self.main_page_url = 'https://qa-scooter.praktikum-services.ru/'
        self.redirect_url = 'https://dzen.ru/?yredirect=true'

    @allure.step('Ожидается открытие новой страницы')
    @allure.description('Проверка нахождения на странице по тексту и url')
    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.main_page_text))
        WebDriverWait(self.driver, 3).until(expected_conditions.url_to_be(self.main_page_url))
        current_url = self.driver.current_url
        assert current_url == self.main_page_url, f"Находимся не на главной странице, текущий URL: {current_url}"

    @allure.step('Кликаем на верхнюю кнопку "Заказать"')
    def click_header_order_button(self):
        self.driver.find_element(*self.header_order_button).click()

    @allure.step('Скролл до кнопки в середине страницы "Заказать"')
    def scroll_to_middle_order_button(self):
        button_element = self.driver.find_element(*self.middle_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button_element)
        time.sleep(1)
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.middle_order_button))

    @allure.step('Клик по кнопке в середине страницы "Заказать"')
    def click_middle_order_button(self):
        self.driver.find_element(*self.middle_order_button).click()

    @allure.step('Клик на логотип "Яндекс"')
    def click_on_logo_yandex(self):
        self.driver.find_element(*self.logo_yandex).click()

    @allure.step('Клик на логотип "Самокат"')
    def click_on_logo_samokat(self):
        self.driver.find_element(*self.logo_samokat).click()

    @allure.step('Ожидания редиректа на страницу')
    def wait_for_redirect_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(self.redirect_url))
        current_url = self.driver.current_url
        assert current_url == self.redirect_url, f"Редирект не выполнен, текущий URL: {current_url}"

    @allure.step('Переключение на вкладку')
    def switch_to_page(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.current_url == url)

    @allure.step('Клик по кнопке "Принять куки"')
    def accept_cookies_button_click(self):
        self.driver.find_element(*self.accept_cookies_button).click()

    @allure.step('Скролл до раздела "Вопросы о важном"')
    def scroll_to_questions_text_header(self):
        text_element = self.driver.find_element(*self.questions_text_header)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", text_element)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.questions_text_header))

    @allure.step('Клик по вопросу по номеру вопроса"')
    def click_question(self, question_number):
        locator = (By.XPATH,
                   f'//div[starts-with(@id, "accordion__heading-{question_number}")'
                   f' and contains(@class, "accordion__button")]')
        self.driver.find_element(*locator).click()

    @allure.step('Проверяем правильность ответа на вопрос по номеру вопроса"')
    def verify_accordion_answer(self, question_number, expected_answer):
        locator = (By.XPATH, f'//div[@id="accordion__panel-{question_number}"]')
        answer_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))
        actual_answer = answer_element.text
        assert actual_answer == expected_answer, f"Ожидаемый ответ '{expected_answer}', но найден '{actual_answer}'" \
                                                 f" для вопроса {question_number}"

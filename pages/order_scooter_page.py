from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage


class OrderScooterPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    SECOND_NAME = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    ADDRESS = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    STATION_SELECT = (By.XPATH, '//div[@class="select-search"]')
    DROPDOWN_STATIONS = (By.XPATH, '//div[@class="select-search__select"]//div')
    TELEPHONE_NUMBER = (By.CSS_SELECTOR, 'input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder="* Телефон: '
                                         'на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")
    ORDER_PAGE_PERSONAL_INFO_TEXT_HEADER = (By.XPATH, '//div[@class="Order_Header__BZXOb" and contains(text(), '
                                                      '"Для кого самокат")]')
    ORDER_PAGE_ABOUT_RENT_TEXT_HEADER = (By.XPATH, '//div[@class="Order_Header__BZXOb" and contains(text(), '
                                                   '"Про аренду")]')
    SCOOTER_DELIVERY_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PERIOD_DROPDOWN_LIST = (By.XPATH, '//div[@class="Dropdown-placeholder"]')
    OFFERED_RENTAL_PERIOD = (By.XPATH, '//div[@class="Dropdown-menu" and @aria-expanded="true"]/div['
                                       '@class="Dropdown-option"]')
    SELECTED_RENTAL_PERIOD = (By.XPATH, "//div[@class='Dropdown-root Order_FilledDate__1pb8n']")
    BLACK_COLOR_CHECHBOX = (By.XPATH, '//label[@for="black" and contains(text(), "чёрный жемчуг")]')
    PLACE_FOR_COMMENT_TO_COURIER = (By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN"]')
    PLACE_FOR_COMMENT_TO_COURIER_FULLFILLED = (By.CSS_SELECTOR, 'input.Input_Input__1iN_Z.Input_Filled__1rDxs'
                                                                '.Input_Responsible__1jDKN[placeholder="Комментарий '
                                                                'для курьера"]')
    ORDER_SCOOTER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and contains(text('
                                      '), "Заказать")]')
    ORDER_MODAL_WINDOW_CONFIRMATION = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    YES_BUTTON_IN_MODAL_WINDOW_CONFIRMATION = (By.XPATH, "//button[contains(text(), 'Да') and contains(@class, "
                                                         "'Button_Button__ra12g')]")
    ORDER_CREATED_MODAL_WINDOW = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    WATCH_THE_STATUS_BUTTON = (By.XPATH, "//button[contains(text(), 'Посмотреть статус') and contains(@class, "
                                         "'Button_Button__ra12g')]")

    @allure.step('Вводим имя в инпут "Имя"')
    def set_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME, first_name)

    @allure.step('Ожидаем, что в инпуте "Имя" корректно отображается введённое значение')
    def check_first_name_value(self, first_name):
        actually_value = self.wait_and_find_element(self.FIRST_NAME).get_property("value")
        expected_value = first_name
        assert actually_value == expected_value, f'Ожидалось значение поля first_name:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Вводим фамилию в инпут "Фамилия"')
    def set_second_name(self, second_name):
        self.enter_text(self.SECOND_NAME, second_name)

    @allure.step('Ожидаем, что в инпуте "Фамилия" корректно отображается введённое значение')
    def check_second_name_value(self, second_name):
        actually_value = self.wait_and_find_element(self.SECOND_NAME).get_property("value")
        expected_value = second_name
        assert actually_value == expected_value, f'Ожидалось значение поля second_name:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Вводим адрес в инпут "Адрес: куда привезти заказ"')
    def set_address(self, address):
        self.enter_text(self.ADDRESS, address)

    @allure.step('Ожидаем, что в инпуте "Адрес" корректно отображается введённое значение')
    def check_address(self, address):
        actually_value = self.wait_and_find_element(self.ADDRESS).get_property("value")
        expected_value = address
        assert actually_value == expected_value, f'Ожидалось значение поля address:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Вводим станцию метро в инпут "Станция метро"')
    def set_metro_station(self, name_metro_station):
        self.click_element(self.STATION_SELECT)
        dropdown_options = self.wait_and_find_elements(self.DROPDOWN_STATIONS)

        for option in dropdown_options:
            if option.text == name_metro_station:
                option.click()
                break

    @allure.step('Вводим срок аренды в инпут "Срок аренды"')
    def set_rental_period(self, rental_period):
        self.click_element(self.PERIOD_DROPDOWN_LIST)
        dropdown_options = self.wait_and_find_elements(self.OFFERED_RENTAL_PERIOD)

        for option in dropdown_options:
            if option.text == rental_period:
                option.click()
                break

    @allure.step('Ожидаем, что в поле "Срок аренды" корректно отображается введённое значение')
    def check_rental_period(self, rental_period):
        actually_value = self.wait_and_find_element(self.SELECTED_RENTAL_PERIOD).text
        expected_value = rental_period
        assert actually_value == expected_value, f'Ожидалось значение поля rental_period:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Ожидаем, что в поле "Станция метро" корректно отображается введённое значение')
    def check_metro_station(self, metro_station):
        actually_value = self.wait_and_find_element(self.METRO_STATION).get_property("value")
        expected_value = metro_station
        assert actually_value == expected_value, f'Ожидалось значение поля metro_station:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Вводим номер телефона в инпут "Номер телефона"')
    def set_telephone_number(self, telephone_number):
        self.enter_text(self.TELEPHONE_NUMBER, telephone_number)

    @allure.step('Ожидаем, что в поле "Телефон" корректно отображается введённое значение')
    def check_telephone_number(self, telephone_number):
        actually_value = self.wait_and_find_element(self.TELEPHONE_NUMBER).get_property("value")
        expected_value = telephone_number
        assert actually_value == expected_value, f'Ожидалось значение поля telephone_number:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Кликаем по кнопке "Далее"')
    def click_next_button(self):
        self.click_element(self.NEXT_BUTTON)

    @allure.step('Ожидаем страницу с вводом персональных данных для заказа')
    def wait_for_order_page_personal_info_header(self):
        self.wait_and_find_element(self.ORDER_PAGE_PERSONAL_INFO_TEXT_HEADER)

    @allure.step('Ожидаем страницу с вводом информации необходимой для заказа')
    def wait_for_order_page_about_rent_text_header(self):
        self.wait_and_find_element(self.ORDER_PAGE_ABOUT_RENT_TEXT_HEADER)

    @allure.step('Вводим срок аренды в инпут "Срок аренды"')
    def set_delivery_date(self, scooter_delivery_date):
        self.enter_text(self.SCOOTER_DELIVERY_DATE, scooter_delivery_date)
        self.click_element(self.ORDER_PAGE_ABOUT_RENT_TEXT_HEADER)

    @allure.step('Ожидаем, что в поле "Срок аренды" корректно отображается введённое значение')
    def check_delivery_date(self, scooter_delivery_date):
        actually_value = self.wait_and_find_element(self.SCOOTER_DELIVERY_DATE).get_property("value")
        expected_value = scooter_delivery_date
        assert actually_value == expected_value, f'Ожидалось значение поля delivery_date:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Кликаем на чекбокс цвета самоката "чёрный жемчуг"')
    def set_black_color_of_scooter(self):
        self.wait_and_find_element(self.BLACK_COLOR_CHECHBOX).click()

    @allure.step('Вводим комментарий в инпут "Комментарий для курьера"')
    def set_comment_for_courier(self, comment_for_courier):
        self.enter_text(self.PLACE_FOR_COMMENT_TO_COURIER, comment_for_courier)

    @allure.step('Ожидаем, что в поле "Комментарий для курьера" корректно отображается введённое значение')
    def check_comment_for_courier(self, comment_for_courier):
        actually_value = self.wait_and_find_element(self.PLACE_FOR_COMMENT_TO_COURIER_FULLFILLED).get_property("value")
        expected_value = comment_for_courier
        assert actually_value == expected_value, f'Ожидалось значение поля comment_for_courier:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Кликаем на кнопку "Заказать" после заполнения анкеты')
    def order_scooter_button_click(self):
        self.click_element(self.ORDER_SCOOTER_BUTTON)

    @allure.step('Ожидаем модального окна подтверждения заказа')
    def wait_for_order_modal_window_confirmation(self):
        self.wait_and_find_element(self.ORDER_MODAL_WINDOW_CONFIRMATION)

    @allure.step('Кликаем "Да" в модальном окне подтверждения заказа')
    def click_confirmation_button_on_modal_window(self):
        self.click_element(self.YES_BUTTON_IN_MODAL_WINDOW_CONFIRMATION)

    @allure.step('Ожидаем модальное окно подтверждения заказа')
    def wait_for_order_created_modal_window(self):
        self.wait_and_find_element(self.ORDER_CREATED_MODAL_WINDOW)

    @allure.step('Кликаем на кнопку "Посмотреть статус"')
    def click_watch_the_status_button(self):
        self.click_element(self.WATCH_THE_STATUS_BUTTON)

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class OrderScooterPage:
    first_name = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    second_name = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    address = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    metro_station = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    station_select = (By.XPATH, '//div[@class="select-search"]')
    dropdown_stations = (By.XPATH, '//div[@class="select-search__select"]//div')
    telephone_number = (By.CSS_SELECTOR, 'input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder="* Телефон: '
                                         'на него позвонит курьер"]')
    next_button = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")
    order_page_personal_info_text_header = (By.XPATH, '//div[@class="Order_Header__BZXOb" and contains(text(), '
                                                      '"Для кого самокат")]')
    order_page_about_rent_text_header = (By.XPATH, '//div[@class="Order_Header__BZXOb" and contains(text(), '
                                                   '"Про аренду")]')
    scooter_delivery_date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    period_dropdown_list = (By.XPATH, '//div[@class="Dropdown-placeholder"]')
    offered_rental_period = (By.XPATH, '//div[@class="Dropdown-menu" and @aria-expanded="true"]/div['
                                       '@class="Dropdown-option"]')
    selected_rental_period = (By.XPATH, "//div[@class='Dropdown-root Order_FilledDate__1pb8n']")
    black_color_chechbox = (By.XPATH, '//label[@for="black" and contains(text(), "чёрный жемчуг")]')
    place_for_comment_to_courier = (By.XPATH, '//input[@class="Input_Input__1iN_Z Input_Responsible__1jDKN"]')
    place_for_comment_to_courier_fullfilled = (By.CSS_SELECTOR, 'input.Input_Input__1iN_Z.Input_Filled__1rDxs'
                                                                '.Input_Responsible__1jDKN[placeholder="Комментарий '
                                                                'для курьера"]')
    order_scooter_button = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and contains(text('
                                      '), "Заказать")]')
    order_modal_window_confirmation = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ']")
    yes_button_in_modal_window_confirmation = (By.XPATH, "//button[contains(text(), 'Да') and contains(@class, "
                                                         "'Button_Button__ra12g')]")
    order_created_modal_window = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    watch_the_status_button = (By.XPATH, "//button[contains(text(), 'Посмотреть статус') and contains(@class, "
                                         "'Button_Button__ra12g')]")

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вводим имя в инпут "Имя"')
    def set_first_name(self, first_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)

    @allure.step('Ожидаем, что в инпуте "Имя" корректно отображается введённое значение')
    def check_first_name_value(self, first_name):
        actually_value = self.driver.find_element(*self.first_name).get_property("value")
        expected_value = first_name
        assert actually_value == expected_value, f'Ожидалось значение поля first_name:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Вводим фамилию в инпут "Фамилия"')
    def set_second_name(self, second_name):
        self.driver.find_element(*self.second_name).send_keys(second_name)

    @allure.step('Ожидаем, что в инпуте "Фамилия" корректно отображается введённое значение')
    def check_second_name_value(self, second_name):
        actually_value = self.driver.find_element(*self.second_name).get_property("value")
        expected_value = second_name
        assert actually_value == expected_value, f'Ожидалось значение поля second_name:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Вводим адрес в инпут "Адрес: куда привезти заказ"')
    def set_address(self, address):
        self.driver.find_element(*self.address).send_keys(address)

    @allure.step('Ожидаем, что в инпуте "Адрес" корректно отображается введённое значение')
    def check_address(self, address):
        actually_value = self.driver.find_element(*self.address).get_property("value")
        expected_value = address
        assert actually_value == expected_value, f'Ожидалось значение поля address:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Вводим станцию метро в инпут "Станция метро"')
    def set_metro_station(self, name_metro_station):
        dropdown_menu = self.driver.find_element(*self.station_select)
        dropdown_menu.click()
        dropdown_options = self.driver.find_elements(*self.dropdown_stations)

        for option in dropdown_options:
            if option.text == name_metro_station:
                option.click()
                break

    @allure.step('Вводим срок аренды в инпут "Срок аренды"')
    def set_rental_period(self, rental_period):
        dropdown_menu = self.driver.find_element(*self.period_dropdown_list)
        dropdown_menu.click()
        dropdown_options = self.driver.find_elements(*self.offered_rental_period)

        for option in dropdown_options:
            if option.text == rental_period:
                option.click()
                break

    @allure.step('Ожидаем, что в поле "Срок аренды" корректно отображается введённое значение')
    def check_rental_period(self, rental_period):
        actually_value = self.driver.find_element(*self.selected_rental_period).text
        expected_value = rental_period
        assert actually_value == expected_value, f'Ожидалось значение поля rental_period:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Ожидаем, что в поле "Станция метро" корректно отображается введённое значение')
    def check_metro_station(self, metro_station):
        actually_value = self.driver.find_element(*self.metro_station).get_property("value")
        expected_value = metro_station
        assert actually_value == expected_value, f'Ожидалось значение поля metro_station:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Вводим номер телефона в инпут "Номер телефона"')
    def set_telephone_number(self, telephone_number):
        self.driver.find_element(*self.telephone_number).send_keys(telephone_number)

    @allure.step('Ожидаем, что в поле "Телефон" корректно отображается введённое значение')
    def check_telephone_number(self, telephone_number):
        actually_value = self.driver.find_element(*self.telephone_number).get_property("value")
        expected_value = telephone_number
        assert actually_value == expected_value, f'Ожидалось значение поля telephone_number:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Кликаем по кнопке "Далее"')
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Ожидаем страницу с вводом персональных данных для заказа')
    def wait_for_order_page_personal_info_header(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_page_personal_info_text_header))

    @allure.step('Ожидаем страницу с вводом информации необходимой для заказа')
    def wait_for_order_page_about_rent_text_header(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_page_about_rent_text_header))

    @allure.step('Вводим срок аренды в инпут "Срок аренды"')
    def set_delivery_date(self, scooter_delivery_date):
        self.driver.find_element(*self.scooter_delivery_date).send_keys(scooter_delivery_date)
        self.driver.find_element(*self.order_page_about_rent_text_header).click()

    @allure.step('Ожидаем, что в поле "Срок аренды" корректно отображается введённое значение')
    def check_delivery_date(self, scooter_delivery_date):
        actually_value = self.driver.find_element(*self.scooter_delivery_date).get_property("value")
        expected_value = scooter_delivery_date
        assert actually_value == expected_value, f'Ожидалось значение поля delivery_date:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Кликаем на чекбокс цвета самоката "чёрный жемчуг"')
    def set_black_color_of_scooter(self):
        self.driver.find_element(*self.black_color_chechbox).click()

    @allure.step('Вводим комментарий в инпут "Комментарий для курьера"')
    def set_comment_for_courier(self, comment_for_courier):
        self.driver.find_element(*self.place_for_comment_to_courier).send_keys(comment_for_courier)

    @allure.step('Ожидаем, что в поле "Комментарий для курьера" корректно отображается введённое значение')
    def check_comment_for_courier(self, comment_for_courier):
        actually_value = self.driver.find_element(*self.place_for_comment_to_courier_fullfilled).get_property("value")
        expected_value = comment_for_courier
        assert actually_value == expected_value, f'Ожидалось значение поля comment_for_courier:' \
                                                 f' "{expected_value}", получено "{actually_value}"'

    @allure.step('Кликаем на кнопку "Заказать" после заполнения анкеты')
    def order_scooter_button_click(self):
        self.driver.find_element(*self.order_scooter_button).click()

    @allure.step('Ожидаем модального окна подтверждения заказа')
    def wait_for_order_modal_window_confirmation(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_modal_window_confirmation))

    @allure.step('Кликаем "Да" в модальном окне подтверждения заказа')
    def click_confirmation_button_on_modal_window(self):
        self.driver.find_element(*self.yes_button_in_modal_window_confirmation).click()

    @allure.step('Ожидаем модальное окно подтверждения заказа')
    def wait_for_order_created_modal_window(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.order_created_modal_window))

    @allure.step('Кликаем на кнопку "Посмотреть статус" и ожидаем перехода на страницу статуса заказа')
    def click_watch_the_status_button(self):
        self.driver.find_element(*self.watch_the_status_button).click()
        assert "track" in self.driver.current_url, "URL не содержит 'track'"

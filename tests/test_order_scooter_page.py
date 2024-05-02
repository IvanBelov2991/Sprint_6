from pages.main_page import MainPage
from pages.order_scooter_page import OrderScooterPage
import allure


class TestOrderScooter:
    @allure.title('Проверка положительного сценария заказа самоката')
    @allure.description('На главной странице проверяем вход на страницу заказа через'
                        ' две кнопки "Заказать", заполняем форму заказа и переходим к странице заказа')
    def test_order_scooter(self, driver, order_data):
        main_page = MainPage(driver)
        order_page = OrderScooterPage(driver)
        first_name, last_name, address, phone_number, metro_station, delivery_date, rental_period, comment = order_data
        main_page.wait_for_load_main_page()
        main_page.accept_cookies_button_click()
        main_page.click_header_order_button()
        order_page.wait_for_order_page_personal_info_header()
        main_page.click_on_logo_samokat()
        main_page.wait_for_load_main_page()
        main_page.scroll_to_middle_order_button()
        main_page.click_middle_order_button()
        order_page.wait_for_order_page_personal_info_header()
        order_page.set_first_name(first_name)
        order_page.set_second_name(last_name)
        order_page.set_address(address)
        order_page.set_telephone_number(phone_number)
        order_page.set_metro_station(metro_station)
        order_page.check_first_name_value(first_name)
        order_page.check_second_name_value(last_name)
        order_page.check_address(address)
        order_page.check_metro_station(metro_station)
        order_page.check_telephone_number(phone_number)
        order_page.click_next_button()
        order_page.wait_for_order_page_about_rent_text_header()
        order_page.set_delivery_date(delivery_date)
        order_page.check_delivery_date(delivery_date)
        order_page.set_rental_period(rental_period)
        order_page.check_rental_period(rental_period)
        order_page.set_black_color_of_scooter()
        order_page.set_comment_for_courier(comment)
        order_page.check_comment_for_courier(comment)
        order_page.order_scooter_button_click()
        order_page.wait_for_order_modal_window_confirmation()
        order_page.click_confirmation_button_on_modal_window()
        order_page.wait_for_order_created_modal_window()
        order_page.click_watch_the_status_button()

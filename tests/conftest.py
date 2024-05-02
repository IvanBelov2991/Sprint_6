import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get('https://qa-scooter.praktikum-services.ru/')
    firefox_driver.maximize_window()
    yield firefox_driver
    firefox_driver.quit()


@pytest.fixture(params=[
    ("Иван", "Петров", "Варшавское шоссе 2к3", "71234567890",
     "Черкизовская", '08.06.2024', 'двое суток', 'Мне нужен скороростной самокат'),
    ("Александр", "Богачев", "Усачева, 13", "71234512345",
     "Ботанический сад", '01.07.2024', 'сутки', 'Мне нужен надежный самокат')
])
def order_data(request):
    return request.param

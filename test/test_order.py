import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:

    @allure.description('Проверяем, что заказ самоката прошел успешно через верхнюю строчку')
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, period, color, comment", [
        ("Ангелина", "Дзен", "ул. Спортивная, д. 59", "Лубянка", "375294569852", "23.01.2024", "сутки", "чёрный жемчуг", "Спасибо"),
        ("Арсений", "Щи", "ул. Маркса, д. 106", "Фрунзенская", "375446587452", "28.10.2024", "двое суток", "серая безысходность", "С любовью")
    ])
    def test_order_form_top(self, driver, name, surname, address, metro, phone, date, period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_order_button_top()
        order_page.fill_order_form(name, surname, address, metro, phone)
        order_page.fill_rental_form(date, period, color, comment)
        assert order_page.check_success_message()

    @allure.description('Проверяем, что заказ самоката прошел успешно через нижнюю кнопку')
    @pytest.mark.parametrize("name, surname, address, metro, phone, date, period, color, comment", [
        ("Ангелина", "Дзен", "ул. Спортивная, д. 59", "Комсомольская", "375294569852", "23.01.2024", "сутки", "чёрный жемчуг", "Спасибо"),
        ("Арсений", "Щи", "ул. Маркса, д. 106", "Красносельская", "375446587452", "28.10.2024", "двое суток", "серая безысходность", "С любовью")
    ])
    def test_order_form_middle(self, driver, name, surname, address, metro, phone, date, period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_order_button_middle()
        order_page.fill_order_form(name, surname, address, metro, phone)
        order_page.fill_rental_form(date, period, color, comment)
        assert order_page.check_success_message()

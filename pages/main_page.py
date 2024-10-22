
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure
class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Клик на верхнюю кнопку заказа')
    def click_order_button_top(self):
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_TOP)


    @allure.step('Клик на среднюю кнопку заказа')
    def click_order_button_middle(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
        self.click_element_with_wait(MainPageLocators.ORDER_BUTTON_MIDDLE)


    @allure.step('Клик на лого скутера')
    def click_scooter_logo(self):
        self.click_element_with_wait(MainPageLocators.SCOOTER_LOGO)


    @allure.step('Клик на лого Яндекса')
    def click_yandex_logo(self):
        self.click_element_with_wait(MainPageLocators.YANDEX_LOGO)

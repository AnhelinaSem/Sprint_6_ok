from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
class OrderPage(BasePage):
    def __init__(self, driver):
        self.driver = driver


    def fill_order_form(self, name, surname, address, metro, phone):
        self.find_element_with_wait(OrderPageLocators.NAME_FIELD).send_keys(name)
        self.find_element_with_wait(OrderPageLocators.SURNAME_FIELD).send_keys(surname)
        self.find_element_with_wait(OrderPageLocators.ADDRESS_FIELD).send_keys(address)
        self.find_element_with_wait(OrderPageLocators.METRO_FIELD).click()
        self.select_from_dropdown(OrderPageLocators.METRO_DROPDOWN_OPTION, metro)
        self.find_element_with_wait(OrderPageLocators.PHONE_FIELD).send_keys(phone)
        self.find_element_with_wait(OrderPageLocators.NEXT_BUTTON).click()


    def fill_rental_form(self, date, period, color, comment):
        date_input = self.wait_for_element_to_be_clickable(OrderPageLocators.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        self.wait_for_element_to_be_invisible((By.CLASS_NAME, "react-datepicker"))
        rental_dropdown = self.wait_for_element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        rental_dropdown.click()
        period_option = self.wait_for_element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']"))
        period_option.click()
        self.click_element(OrderPageLocators.COLOR_CHECKBOX)
        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)
        order_button = self.wait_for_element_to_be_clickable(OrderPageLocators.ORDER_BUTTON)
        if order_button:
            order_button.click()


    def check_success_message(self):
        return self.find_element_with_wait(OrderPageLocators.SUCCESS_MESSAGE).is_displayed()



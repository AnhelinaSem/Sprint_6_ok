from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def handle_cookie_consent(self):
        try:
            cookie_consent = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located((By.CLASS_NAME, "App_CookieConsent__1yUIN"))
            )
            accept_button = cookie_consent.find_element(By.XPATH, ".//button[contains(text(), 'да')]")
            accept_button.click()
        except:

            pass

    def fill_order_form(self, name, surname, address, metro, phone):
        self.handle_cookie_consent()
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)
        self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(surname)
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)
        self.driver.find_element(*OrderPageLocators.METRO_FIELD).click()
        metro_options = self.driver.find_elements(*OrderPageLocators.METRO_DROPDOWN_OPTION)
        for option in metro_options:
            if option.text == metro:
                WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(option)).click()
                break
        self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def fill_rental_form(self, date, period, color, comment):

        date_input = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(OrderPageLocators.DATE_INPUT)
        )
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located((By.CLASS_NAME, "react-datepicker"))
        )

        rental_dropdown = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        )
        rental_dropdown.click()

        period_option = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']"))
        )
        period_option.click()

        self.driver.find_element(*OrderPageLocators.COLOR_CHECKBOX).click()

        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)

        order_button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(OrderPageLocators.ORDER_BUTTON)
        )
        order_button.click()

    def check_success_message(self):
        return self.driver.find_element(*OrderPageLocators.SUCCESS_MESSAGE).is_displayed()


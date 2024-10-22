from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def find_element_with_wait(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located(locator)
            )
            return element
        except Exception as e:
            print(f"Error finding element: {locator}, Exception: {e}")
            return None


    def click_element_with_wait(self, locator):
        element = self.scroll_to_element(locator)
        if element:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(locator)
            )
            element.click()
        else:
            print(f"Element not clickable: {locator}")


    def select_from_dropdown(self, dropdown_locator, option_text):
        self.find_element_with_wait(dropdown_locator).click()
        options = self.driver.find_elements(*dropdown_locator)
        for option in options:
            if option.text == option_text:
                self.scroll_to_element(option)
                WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(option)).click()
                break


    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        else:
            print(f"Element not found: {locator}")
        return element


    def wait_for_element_to_be_clickable(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(locator)
            )
            return element
        except Exception as e:
            print(f"Element not clickable: {locator}, Exception: {e}")
            return None


    def wait_for_element_to_be_invisible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.invisibility_of_element_located(locator)
            )
        except Exception as e:
            print(f"Element not invisible: {locator}, Exception: {e}")


    def click_element(self, locator):
        element = self.find_element_with_wait(locator)
        if element:
            element.click()
        else:
            print(f"Element not found: {locator}")


    def send_keys_to_element(self, locator, keys):
        element = self.find_element_with_wait(locator)
        if element:
            element.clear()
            element.send_keys(keys)
        else:
            print(f"Element not found: {locator}")


    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])


    def get_current_url(self):
        return self.driver.current_url

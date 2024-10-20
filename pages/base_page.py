from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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



    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        else:
            print(f"Element not found: {locator}")
        return element



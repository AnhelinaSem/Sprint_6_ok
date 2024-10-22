from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = By.XPATH, '//button[contains(@class, "Button_Button")]'
    ORDER_BUTTON_MIDDLE = By.XPATH, '//button[contains(@class, "Button_Button") and contains(@class, "Button_Middle")]'
    SCOOTER_LOGO = By.XPATH, '//img[@alt="Scooter"]'
    YANDEX_LOGO = By.XPATH, '//img[@alt="Yandex"]'
    FAQ_QUESTIONS = By.XPATH, '//*[@id="accordion__heading-{}"]'
    FAQ_ANSWERS = By.XPATH, '//*[@id="accordion__panel-{}"]'
    LAST_QUESTION = (By.XPATH, "//div[@id='accordion__heading-7']")

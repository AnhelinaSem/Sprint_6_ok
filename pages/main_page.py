
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver


    def click_to_question(self, locator_q_formatted):
        question_element = self.find_element_with_wait(locator_q_formatted)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question_element)
        self.driver.execute_script("arguments[0].click();", question_element)


    def get_answer_text_1(self, locator_a_formatted):
        return self.get_text_from_element(locator_a_formatted)



    def get_answer_text(self, num):
        self.scroll_to_element(MainPageLocators.LAST_QUESTION)
        question = self.find_element_with_wait(MainPageLocators.FAQ_QUESTIONS[num])
        question.click()
        answer = self.find_element_with_wait(MainPageLocators.FAQ_ANSWERS[num])
        return answer.text




    def click_order_button_top(self):

        self.driver.find_element_with_wait(MainPageLocators.ORDER_BUTTON_TOP).click()

    def click_order_button_middle(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_MIDDLE)
        self.driver.find_element_with_wait(*MainPageLocators.ORDER_BUTTON_MIDDLE).click()



    def click_scooter_logo(self):

        self.driver.find_element_with_wait(MainPageLocators.SCOOTER_LOGO).click()

    def click_yandex_logo(self):

        self.driver.find_element_with_wait(MainPageLocators.YANDEX_LOGO).click()
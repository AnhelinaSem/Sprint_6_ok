import pytest
import allure
from pages.main_page import MainPage, MainPageLocators
from data import ANSWER_TEXTS

@allure.description(
        'Проверяем соответствие ответов на вопросы')
@pytest.mark.parametrize(
    'num, expected_answer',
    [(i, text) for i, text in enumerate(ANSWER_TEXTS)]
)
def test_questions_and_answers(driver, num, expected_answer):
    main_page = MainPage(driver)
    question_locator = (MainPageLocators.FAQ_QUESTIONS[0], MainPageLocators.FAQ_QUESTIONS[1].format(num))
    answer_locator = (MainPageLocators.FAQ_ANSWERS[0], MainPageLocators.FAQ_ANSWERS[1].format(num))
    main_page.click_element_with_wait(question_locator)
    answer = main_page.find_element_with_wait(answer_locator)
    assert answer.text == expected_answer

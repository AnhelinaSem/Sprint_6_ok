import allure
import pytest
from pages.main_page import MainPage
from data import ANSWER_TEXTS


class TestMainPage:

    @allure.description('Проверяем, что при клике на вопрос ответ правильный')
    @pytest.mark.parametrize(
        'num, expected_answer',
        [
            (0, ANSWER_TEXTS[0]),
            (1, ANSWER_TEXTS[1]),
            (2, ANSWER_TEXTS[2]),
            (3, ANSWER_TEXTS[3]),
            (4, ANSWER_TEXTS[4]),
            (5, ANSWER_TEXTS[5]),
            (6, ANSWER_TEXTS[6]),
            (7, ANSWER_TEXTS[7])
        ]
    )
    def test_questions_and_answers(self, driver, num, expected_answer):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(num) == expected_answer


import allure
import pytest
from pages.main_page import MainPage

class TestLogo:

    @allure.description(
        'Проверяем клик на лого:самоат и Яндекс')

    @allure.step('Проверяем, что при клик на лого «Самокат» переход на главную стр')
    def test_logo_samokat(self, driver):
        main_page = MainPage(driver)

        # логотип «Самокат»
        main_page.click_scooter_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.step('Проверяем, что при клик на лого Яндекс открывается страница дзен')
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        # логотип Яндекса
        main_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[-1])
        assert "dzen.ru" in driver.current_url


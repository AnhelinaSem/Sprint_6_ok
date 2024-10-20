import pytest
from selenium import webdriver
from src.config import Config

@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    if Config.FULLSCREEN:
        chrome_options.add_argument("--start-maximized")
    chrome = webdriver.Chrome(options=chrome_options)
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()
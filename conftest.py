import pytest
from selenium import webdriver
from config import WINDOW_SIZE


@pytest.fixture(scope="function")
def driver():
    """Фикстура для автоматического запуска и закрытия браузера."""
    options = webdriver.ChromeOptions()
    options.add_argument(WINDOW_SIZE)

    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()

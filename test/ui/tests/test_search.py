import pytest
import allure
from selenium import webdriver
from config import UI_BASE_URL, WINDOW_SIZE, BOOK_TITLE
from SearchPage import SearchPage


@allure.title("Поиск книги по названию через поисковую строку с переходом на результаты")
@allure.description("Проверяет корректную работу поисковой строки и динамических подсказок.")
@allure.feature("Каталог и Поиск")
@allure.story("Поиск товаров в каталоге")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ui
def test_searh() -> None:
    options = webdriver.ChromeOptions()
    options.add_argument(WINDOW_SIZE)
    driver = webdriver.Chrome(options=options)

    search = SearchPage(driver, UI_BASE_URL)

    search.open_main_page()
    search.enter_search_query(BOOK_TITLE)
    search.click_on_suggest_link(BOOK_TITLE)
    search.wait_for_search_results_page()

    with allure.step("Проверить, что текущий URL содержит подстроку '/search'"):
        assert "search" in driver.current_url, f"Тест упал. Текущий URL: {driver.current_url}"

        with allure.step("Закрыть сессию браузера"):
            driver.quit()

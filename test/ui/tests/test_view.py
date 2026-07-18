import pytest
import allure
from selenium import webdriver
from config import UI_BASE_URL, WINDOW_SIZE, BOOK_TITLE
from ViewPage import ViewPage


@allure.title("Просмотр карточки товара")
@allure.description("Проверяет корректное открытие страницы товара после клика по его обложке в результатах поиска.")
@allure.feature("Каталог и Поиск")
@allure.story("Поиск и просмотр карточки товара")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_view_product_card() -> None:
    options = webdriver.ChromeOptions()
    options.add_argument(WINDOW_SIZE)
    driver = webdriver.Chrome(options=options)

    view = ViewPage(driver, UI_BASE_URL)

    view.open_main_page()
    view.enter_search_query(BOOK_TITLE)
    view.click_on_suggest_link(BOOK_TITLE)

    view.click_on_book_image(BOOK_TITLE)

    actual_title: str = view.get_product_detail_title()

    with allure.step(f"Проверить, что заголовок на карточке товара содержит '{BOOK_TITLE}'"):
        assert BOOK_TITLE in actual_title, f"Ожидали '{BOOK_TITLE}', но получили '{actual_title}'"

    with allure.step("Закрыть сессию браузера"):
        driver.quit()

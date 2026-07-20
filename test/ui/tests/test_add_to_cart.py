import pytest
import allure
from config import BOOK_TITLE, BOOK_URL
from test.ui.pages.AddToCartPage import AddToCartPage


@allure.title("Добавление книги в корзину со страницы товара")
@allure.description("Проверяет, что при клике на 'Купить' на странице книги товар добавляется в корзину, а кнопка меняется на 'Оформить'.")
@allure.feature("Корзина")
@allure.story("Управление товарами в корзине")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_card_l(driver) -> None:
    cart_page = AddToCartPage(driver, BOOK_URL)

    cart_page.open_product_page()
    cart_page.verify_book_title_on_page(BOOK_TITLE)
    cart_page.click_buy_button()

    button_text: str = cart_page.get_cart_button_text()

    with allure.step("Проверить, что текст кнопки изменился на 'Оформить'"):
        assert "Оформить" in button_text, f"Ожидали текст 'Оформить', но получили '{button_text}'"

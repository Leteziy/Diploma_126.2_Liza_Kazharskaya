import pytest
import allure
from config import SEARCH_PAGE_URL
from test.ui.pages.CartCleanPage import CartCleanPage


@allure.title("Полная очистка корзины")
@allure.description("Проверяет, что после добавления товара кнопка 'Очистить корзину' успешно удаляет все позиции.")
@allure.feature("Корзина")
@allure.story("Управление товарами в корзине")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_clear_all_cart(driver) -> None:
    cart_manager = CartCleanPage(driver, SEARCH_PAGE_URL)

    cart_manager.open_search_page()
    cart_manager.add_product_to_cart()
    cart_manager.click_cart_icon()
    cart_manager.click_clear_cart_button()

    is_message_visible: bool = cart_manager.is_empty_cart_message_displayed()

    with allure.step("Убедиться, что на экране отображается сообщение 'Корзина очищена'"):
        assert is_message_visible, "Сообщение о пустой корзине не появилось после её очистки!"

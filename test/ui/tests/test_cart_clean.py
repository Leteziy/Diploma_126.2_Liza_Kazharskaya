import pytest
import allure
from selenium import webdriver
from config import WINDOW_SIZE, SEARCH_PAGE_URL, CART_PAGE_URL
from CartCleanPage import CartCleanPage


@allure.title("Полная очистка корзины")
@allure.description("Проверяет, что после добавления товара кнопка 'Очистить корзину' успешно удаляет все позиции.")
@allure.feature("Корзина")
@allure.story("Управление товарами в корзине")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_clear_all_cart() -> None:
    # Настройка браузера
    options = webdriver.ChromeOptions()
    options.add_argument(WINDOW_SIZE)
    driver = webdriver.Chrome(options=options)

    cart_manager = CartCleanPage(driver, SEARCH_PAGE_URL, CART_PAGE_URL)

    cart_manager.open_search_page()
    cart_manager.add_product_to_cart()
    cart_manager.open_cart_page()
    cart_manager.click_clear_cart_button()

    is_message_visible: bool = cart_manager.is_empty_cart_message_displayed()

    with allure.step("Убедиться, что на экране отображается сообщение 'Корзина очищена'"):
        assert is_message_visible, "Сообщение о пустой корзине не появилось после её очистки!"

    with allure.step("Закрыть сессию браузера"):
        driver.quit()

import pytest
import allure
from selenium import webdriver
from config import UI_BASE_URL, WINDOW_SIZE
from GoToCartPage import GoToCartPage


@allure.title("Переход в корзину с главной страницы")
@allure.description("Проверяет, что при клике на кнопку 'Корзина' пользователь успешно перенаправляется в раздел корзины.")
@allure.feature("Корзина")
@allure.story("Навигация по сайту")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ui
def test_go_to_cart_page() -> None:
    options = webdriver.ChromeOptions()
    options.add_argument(WINDOW_SIZE)
    driver = webdriver.Chrome(options=options)

    navigation = GoToCartPage(driver, UI_BASE_URL)

    navigation.open_main_page()
    navigation.click_cart_button()
    navigation.wait_for_cart_page()

    with allure.step("Проверить, что текущий URL содержит подстроку 'cart'"):
        assert "cart" in driver.current_url, f"Тест упал. Текущий URL: {driver.current_url}"

    with allure.step("Закрыть сессию браузера"):
        driver.quit()

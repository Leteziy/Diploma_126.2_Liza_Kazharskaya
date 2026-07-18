import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartCleanPage:
    """Класс для управления товарами в корзине и её полной очистки."""

    def __init__(self, driver: WebDriver, search_url: str, cart_url: str) -> None:
        """Инициализация драйвера, URL-адресов и явных ожиданий."""
        self.driver: WebDriver = driver
        self.search_url: str = search_url
        self.cart_url: str = cart_url
        self.wait: WebDriverWait = WebDriverWait(self.driver, 20)

    @allure.step("Открыть страницу результатов поиска с товаром")
    def open_search_page(self) -> None:
        """Переходит по URL на результаты поиска."""
        self.driver.get(self.search_url)

    @allure.step("Скроллить к кнопке 'Купить' и добавить книгу в корзину")
    def add_product_to_cart(self) -> None:
        """Находит кнопку 'Купить', скроллит страницу, чтобы избежать баннеров и кликает по ней."""
        buy_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Купить')]"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(buy_button).perform()
        actions.scroll_by_amount(0, 150).perform()

        self.wait.until(EC.element_to_be_clickable(buy_button))
        buy_button.click()

    @allure.step("Перейти на страницу корзины")
    def open_cart_page(self) -> None:
        """Переходит по URL непосредственно в корзину."""
        self.driver.get(self.cart_url)

    @allure.step("Кликнуть по кнопке 'Очистить корзину'")
    def click_clear_cart_button(self) -> None:
        """Дожидается доступности кнопки полной очистки и осуществляет клик."""
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid-button-cart="clearAll"]'))
        ).click()

    @allure.step("Проверить появление сообщения о пустой корзине")
    def is_empty_cart_message_displayed(self) -> bool:
        """Проверяет видимость текста 'Корзина очищена' на экране."""
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Корзина очищена')]"))
        ).is_displayed()

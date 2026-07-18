import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class GoToCartPage:
    """Класс для работы с навигацией и шапкой главной страницы Читай-Города."""

    def __init__(self, driver: WebDriver, url: str) -> None:
        """Инициализация драйвера, базового URL-адреса и явных ожиданий."""
        self.driver: WebDriver = driver
        self.url: str = url
        self.wait: WebDriverWait = WebDriverWait(self.driver, 15)

    @allure.step("Открыть главную страницу сайта")
    def open_main_page(self) -> None:
        """Открывает интернет-магазин по переданному URL."""
        self.driver.get(self.url)

    @allure.step("Кликнуть по кнопке 'Корзина' в шапке сайта")
    def click_cart_button(self) -> None:
        """Находит кнопку корзины по тексту в XPath и кликает на неё в одну строку."""
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Корзина')]"))
        ).click()

    @allure.step("Ожидание перехода на страницу корзины")
    def wait_for_cart_page(self) -> bool:
        """Проверяет, что URL-адрес изменился и теперь содержит подстроку 'cart'."""
        return self.wait.until(EC.url_contains("cart"))

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class ViewPage:
    """Класс для работы с главной страницей Читай-Города."""

    def __init__(self, driver: WebDriver, url: str) -> None:
        """Инициализация драйвера, целевого URL-адреса и явных ожиданий."""
        self.driver: WebDriver = driver
        self.url: str = url
        self.wait: WebDriverWait = WebDriverWait(self.driver, 15)

    @allure.step("Открыть главную страницу сайта")
    def open_main_page(self) -> None:
        """Этот метод открывает онлайн-магазин по переданному URL."""
        self.driver.get(self.url)

    @allure.step("Ввести название книги в строку поиска")
    def enter_search_query(self, book_title: str) -> None:
        """Этот метод находит строку поиска по ID и вводит текст."""
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "app-search"))
        ).send_keys(book_title)

    @allure.step("Кликнуть по поисковой подсказке в выпадающем списке")
    def click_on_suggest_link(self, book_title: str) -> None:
        """Метод осуществляет клик по подсказке."""
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'[data-testid-suggest-link="{book_title}"]'))
        ).click()

    @allure.step("Кликнуть по обложке книги в результатах поиска")
    def click_on_book_image(self, book_title: str) -> None:
        """Находит изображение книги по её названию в атрибуте alt и кликает на него."""
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'img[alt="{book_title}"]'))
        ).click()

    @allure.step("Получить название книги с открывшейся карточки товара")
    def get_product_detail_title(self) -> str:
        """Дожидается появления заголовка на карточке товара и возвращает его текстовое значение."""
        return self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-detail-page__title"))
        ).text

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class AddToCartPage:
    """Класс для работы с карточкой товара и добавлением его в корзину."""

    def __init__(self, driver: WebDriver, url: str) -> None:
        """Инициализация драйвера, ссылки на товар и явных ожиданий."""
        self.driver: WebDriver = driver
        self.url: str = url
        self.wait: WebDriverWait = WebDriverWait(self.driver, 15)

    @allure.step("Перейти на страницу книги ссылке")
    def open_product_page(self) -> None:
        """Метод открывает страницу товара по переданному URL."""
        self.driver.get(self.url)

    @allure.step("Дождаться появления заголовка книги на странице")
    def verify_book_title_on_page(self, book_title: str) -> None:
        """Проверяет наличие ожидаемого названия книги в теге h1."""
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1"), book_title)
        )

    @allure.step("Скроллить страницу до кнопки 'Купить' и кликнуть по ней")
    def click_buy_button(self) -> None:
        """Находит кнопку 'Купить', скроллит к ней экран, для того чтобы кнопку не перекрывали баннеры и кликает ее."""
        buy_button = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@type='button']//div[contains(text(), 'Купить')]")
            )
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(buy_button).perform()
        actions.scroll_by_amount(0, 150).perform()

        self.wait.until(EC.element_to_be_clickable(buy_button))
        buy_button.click()

    @allure.step("Получить текст кнопки корзины после добавления товара")
    def get_cart_button_text(self) -> str:
        """Дожидается изменения состояния кнопки на 'Оформить' и возвращает текст."""
        return self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-testid-button-mini-product-card="inCart"]')
            )
        ).text

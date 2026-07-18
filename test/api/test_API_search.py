import requests
import pytest
import allure
from config import BASE_URL, MY_HEADERS


@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Каталог и Поиск")
@allure.story("Поиск товаров в каталоге")
@allure.title("Поиск книги по названию через API")
def test_search_product_short_url() -> None:
    """Тест: Поиск книги по короткому URL-адресу с минимальным набором параметров."""

    with allure.step("Сформировать URL-адрес поиска с query-параметрами"):
        search_phrase: str = "самые умные птицы на свете вороны"
        url: str = (
            f"{BASE_URL}api/v2/search/product"
            "?products[page]=1"  # Показать 1 страницу результатов
            "&products[per-page]=10"  # Максимум 10 книг
            f"&phrase={search_phrase}"
        )

    with allure.step(f"Отправить GET-запрос на поиск книги по названию книги: '{search_phrase}'"):
        headers_dict: dict[str, str] = MY_HEADERS
        response: requests.Response = requests.get(url, headers=headers_dict)

    with allure.step("Проверить, что сервер выполнил запрос и вернул успешный статус-код 200 OK"):
        assert response.status_code == 200

import requests
import pytest
import allure
from config import BASE_URL, TOKEN


@pytest.mark.api
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Каталог и Поиск")
@allure.story("Негативные проверки API каталога")
@allure.title("Запрос информации о книги без названия")
def test_get_product_without_slug() -> None:
    """Проверяем, что запрос без указания названия книги возвращает ошибку 404 (Not Found)."""

    with allure.step("Подготовить URL без указания slug книги и заголовки авторизации"):
        url: str = f"{BASE_URL}api/v1/products/"
        headers: dict[str, str] = {
            "Accept": "application/json",
            "Authorization": f"Bearer {TOKEN}"
        }

    with allure.step("Отправляем GET-запрос на эндпоинт без параметра slug"):
        response: requests.Response = requests.get(url, headers=headers)

    with allure.step("Проверить, что сервер вернул статус-код 404 Not Found"):
        assert response.status_code == 404

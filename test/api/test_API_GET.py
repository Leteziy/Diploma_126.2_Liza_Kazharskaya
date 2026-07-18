import requests
import pytest
import allure
from config import BASE_URL, TOKEN


@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Каталог и Поиск")
@allure.story("Получение информации о товаре")
@allure.title("Успешное получение информации о книге по названию")
def test_get_d() -> None:
    """Тест проверяет успешное получение информации о товаре по его названию."""

    with allure.step("Подготовить URL и заголовки авторизации для API-запроса"):
        url: str = f"{BASE_URL}api/v1/products/slug/samye-umnye-pticy-na-svete-vorony-3148840"
        headers: dict[str, str] = {
            "Accept": "application/json",
            "Authorization": f"Bearer {TOKEN}"
        }

    with allure.step("Отправляем GET-запрос на получение данных о книге"):
        response: requests.Response = requests.get(url, headers=headers)

    with allure.step("Проверить, запрос прошел и что сервер вернул статус-код 200 OK"):
        assert response.status_code == 200

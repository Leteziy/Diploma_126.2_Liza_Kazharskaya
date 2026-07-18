import requests
import pytest
import allure
from config import BASE_URL


@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Каталог и Поиск")
@allure.story("Негативные проверки API каталога")
@allure.title("Просмотр книги без токена авторизации")
def test_get_product_without_token() -> None:
    """Проверяем, вернет ли сервер ошибку при отсутствии заголовка Authorization."""

    with allure.step("Подготовить URL и заголовки запроса без параметра Authorization"):
        product_slug: str = "samye-umnye-pticy-na-svete-vorony-3148840"
        url: str = f"{BASE_URL}api/v1/products/slug/{product_slug}"
        headers: dict[str, str] = {"Accept": "application/json"}

    with allure.step(f"Отправить GET-запрос для slug '{product_slug}' без токена"):
        response: requests.Response = requests.get(url, headers=headers)

    with allure.step("Проверить, что сервер отклонил запрос с кодом 401 Unauthorized"):
        assert response.status_code == 401

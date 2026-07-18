import requests
import pytest
import allure
from config import BASE_URL, TOKEN


@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Корзина")
@allure.story("Управление товарами в корзине")
@allure.title("Добавление книги в корзину через API")
def test_add_product_to_cart() -> None:
    """Тест: Добавление книги в корзину через метод POST /v1/cart/product."""

    with allure.step("Подготавливаем параметры, заголовки и payload для POST-запроса"):
        url: str = f"{BASE_URL}api/v1/cart/product"
        my_headers: dict[str, str] = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}",
        }
        payload: dict[str, int] = {"id": 3148840}

    with allure.step("Отправить POST-запрос на добавление книги по id в корзину"):
        response: requests.Response = requests.post(url, headers=my_headers, json=payload)

    with allure.step("Проверить, что сервер вернул успешный статус-код"):
        assert response.status_code in [200, 201]

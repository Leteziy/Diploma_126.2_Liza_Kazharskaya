import requests
import pytest
import allure
from config import BASE_URL, TOKEN


@pytest.mark.api
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Корзина")
@allure.story("Негативные проверки API корзины")
@allure.title("Добавление в корзину книги с несуществующим id")
def test_add_product_to_cart_invalid_id() -> None:
    """Тест: Проверка добавления книги в корзину с заведомо некорректным ID."""

    with allure.step("Подготовить параметры, заголовки и невалидный payload для POST-запроса"):
        url: str = f"{BASE_URL}api/v1/cart/product"
        my_headers: dict[str, str] = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}",
        }
        payload: dict[str, int] = {"id": 88005353535}

    with allure.step("Отправить POST-запрос на добавление книги с несуществующим в корзину"):
        response: requests.Response = requests.post(url, headers=my_headers, json=payload)

    with allure.step("Проверить, что сервер вернул код ошибки (400 или 403)"):
        assert response.status_code in [400, 403]

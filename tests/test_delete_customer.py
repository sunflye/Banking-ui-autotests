import allure

from config import url, MANAGER_PATH
from pages.customer_page import CustomersPage


@allure.title("Удаление клиента с именем, длина которого ближе всего к среднему")
def test_delete_customer(browser) -> None:
    """
    Тест на удаление клиента с именем, длина которого ближе всего к среднему значению.
    Проверяет, что после удаления этого клиента его имя отсутствует в таблице.
    """
    page = CustomersPage(browser)
    page.open(url(MANAGER_PATH))
    page.go_to_customers_tab()
    closest_name = page.get_name_closest_to_average_length()
    assert closest_name, "Нет имен"

    page.delete_customer(closest_name)
    updated_names = page.get_first_names()
    assert closest_name not in updated_names, f"Клиент {closest_name} не был удалён!"

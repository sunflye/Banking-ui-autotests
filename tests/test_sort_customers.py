import allure

from config import url, MANAGER_PATH
from pages.customer_page import CustomersPage


@allure.title("Сортировка клиентов по имени (First Name) в таблице")
def test_sort_customers(browser) -> None:
    """
    Тест на сортировку клиентов по имени в таблице.
    Проверяет сортировку по убыванию и возрастанию.
    """
    page = CustomersPage(browser)
    page.open(url(MANAGER_PATH))
    page.go_to_customers_tab()
    first_names_beginning = page.get_first_names()
    assert (
        len(first_names_beginning) >= 3
    ), "В таблице должно быть минимум 3 клиента для проверки сортировки!"

    page.sort_by_first_name()
    first_names_desc = page.get_first_names()
    assert first_names_desc == sorted(
        first_names_desc, reverse=True
    ), "Таблица не отсортирована по убыванию!"

    page.sort_by_first_name()
    first_names_asc = page.get_first_names()
    assert first_names_asc == sorted(
        first_names_asc
    ), "Таблица не отсортирована по возрастанию!"

from pages.customer_page import CustomersPage

from waits import Waits

URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"


def test_delete_customer(browser) -> None:
    """
    Тест на удаление клиента с именем, длина которого ближе всего к среднему значению.
    """
    page = CustomersPage(browser)
    page.open(URL)
    page.go_to_customers_tab()
    first_names = page.get_first_names()
    assert first_names, "Нет имен"

    lengths = [len(name) for name in first_names]
    average = sum(lengths) / len(lengths)
    closest_name = min(first_names, key=lambda name: abs(len(name) - average))
    page.delete_customer(closest_name)

    Waits.for_element(
        browser,
        (page.ROWS),
        timeout=5,
    )
    updated_names = page.get_first_names()
    assert closest_name not in updated_names, f"Клиент {closest_name} не был удалён!"

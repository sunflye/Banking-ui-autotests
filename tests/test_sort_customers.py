from pages.customer_page import CustomersPage
from waits import Waits

URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"


def test_sort_customers(browser):
    page = CustomersPage(browser)
    page.open(URL)
    page.go_to_customers_tab()
    first_names_beginning = page.get_first_names()
    assert (
        len(first_names_beginning) >= 3
    ), "В таблице должно быть минимум 3 клиента для проверки сортировки!"

    page.sort_by_first_name()

    Waits.for_elements(browser, page.ROWS, timeout=5)
    first_names_desc = page.get_first_names()
    assert first_names_desc == sorted(
        first_names_desc, reverse=True
    ), "Таблица не отсортирована по убыванию!"

    page.sort_by_first_name()

    Waits.for_elements(browser, page.ROWS, timeout=5)
    first_names_asc = page.get_first_names()
    assert first_names_asc == sorted(
        first_names_asc
    ), "Таблица не отсортирована по возрастанию!"

import random
import string

from pages.add_customer_page import AddCustomerPage
from pages.customer_page import CustomersPage

URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"


def generate_post_code() -> str:
    """
    Генерирует случайный код из 10 цифр.
    """
    return "".join(random.choices(string.digits, k=10))


def post_code_to_first_name(post_code: str) -> str:
    """
    Преобразует  код в строку, которую можно использовать как имя.
    """
    first_name = ""
    for i in range(0, 10, 2):
        pair = int(post_code[i : i + 2])
        letter = chr(ord("a") + (pair % 26))
        first_name += letter
    return first_name


def test_add_customer(browser) -> None:
    """
    Тест на добавление клиента и проверку его наличия в таблице клиентов.
    """
    post_code = generate_post_code()
    first_name = post_code_to_first_name(post_code)
    add_page = AddCustomerPage(browser)
    add_page.open(URL)
    add_page.add_customer(first_name, first_name, post_code)

    customers_page = CustomersPage(browser)
    customers_page.go_to_customers_tab()
    first_names = customers_page.get_first_names()
    assert first_name in first_names, f"Клиент {first_name} не найден в таблице!"

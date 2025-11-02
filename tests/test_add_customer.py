import allure

from config import url, MANAGER_PATH
from utils import generate_post_code, post_code_to_first_name
from pages.add_customer_page import AddCustomerPage
from pages.customer_page import CustomersPage


@allure.title("Добавление нового клиента через форму Add Customer")
def test_add_customer(browser) -> None:
    """
    Тест на добавление нового клиента через форму Add Customer и проверку его наличия в таблице клиентов.
    """
    post_code = generate_post_code()
    first_name = post_code_to_first_name(post_code)
    add_page = AddCustomerPage(browser)
    add_page.open(url(MANAGER_PATH))
    add_page.add_customer(first_name, first_name, post_code)

    alert_text = add_page.get_alert_text()
    assert "Customer added successfully" in alert_text, "Alert text mismatch"
    add_page.accept_alert()

    customers_page = CustomersPage(browser)
    customers_page.go_to_customers_tab()
    first_names = customers_page.get_first_names()
    assert first_name in first_names, f"Клиент {first_name} не найден в таблице!"

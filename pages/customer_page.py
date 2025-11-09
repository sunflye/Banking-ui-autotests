import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CustomersPage(BasePage):
    """
    Page Object для страницы клиентов.
    Инкапсулирует работу с таблицей клиентов: переход, сортировка, удаление и получение имён.
    """

    CUSTOMERS_BTN = (By.CSS_SELECTOR, 'button[ng-class="btnClass3"]')
    ROWS = (By.CSS_SELECTOR, "table.table-bordered.table-striped tbody tr")
    DELETE_BTN = (By.XPATH, ".//button[contains(text(), 'Delete')]")
    FIRST_NAME_HEADER = (By.XPATH, "//a[contains(text(), 'First Name')]")
    FIRST_NAME_CELL = (By.TAG_NAME, "td")

    @allure.step("Переход на вкладку клиентов.")
    def go_to_customers_tab(self) -> None:
        """
        Переходит на вкладку клиентов и ожидает загрузки таблицы.
        """
        self.click(self.CUSTOMERS_BTN)
        self.find_elements(self.ROWS, timeout=5)

    @allure.step("Получение списка имён клиентов")
    def get_first_names(self) -> list:
        """
        Получает список имён из первой колонки таблицы клиентов.
        """
        table_rows = self.find_elements(self.ROWS)
        first_names = []
        for row in table_rows:
            cells = self.find_child_elements(row, *self.FIRST_NAME_CELL)
            if cells:
                first_names.append(cells[0].text)
        return first_names

    @allure.step("Сортировка клиентов по имени")
    def sort_by_first_name(self) -> None:
        """
        Кликает по заголовку "First Name" для сортировки таблицы.
        """
        self.click(self.FIRST_NAME_HEADER)

    @allure.step("Удаление клиента с именем: {name_to_delete}")
    def delete_customer(self, name_to_delete: str) -> None:
        """
        Удаляет клиента по имени из таблицы.
        """
        table_rows = self.find_elements(self.ROWS)
        for row in table_rows:
            cells = self.find_child_elements(row, *self.FIRST_NAME_CELL)
            if cells and cells[0].text == name_to_delete:
                delete_btn = self.find_child_element(row, *self.DELETE_BTN)
                delete_btn.click()
                break

    @allure.step("Поиск имени, длина которого ближе всего к среднему")
    def get_name_closest_to_average_length(self) -> str | None:
        """
        Возвращает имя, длина которого ближе всего к среднему арифметическому длин всех имён.
        """
        first_names = self.get_first_names()
        if not first_names:
            return None
        lengths = [len(name) for name in first_names]
        average = sum(lengths) / len(lengths)
        return min(first_names, key=lambda name: abs(len(name) - average))

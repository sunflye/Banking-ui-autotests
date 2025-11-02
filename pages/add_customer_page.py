import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AddCustomerPage(BasePage):
    """
    Page Object для страницы добавления клиента.
    Инкапсулирует работу с формой "Add Customer".
    """

    ADD_CUSTOMER_BTN = (By.CSS_SELECTOR, 'button[ng-class="btnClass1"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='fName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='lName']")
    POST_CODE_INPUT = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    @allure.step("Переход на вкладку добавления клиента")
    def go_to_add_customer_tab(self) -> None:
        """
        Переходит на вкладку добавления клиента.
        """
        self.click(self.ADD_CUSTOMER_BTN)

    @allure.step("Добавление клиента: {first_name} {last_name}, Post Code: {post_code}")
    def add_customer(self, first_name: str, last_name: str, post_code: str) -> None:
        """
        Заполняет форму добавления клиента и отправляет её.
        """
        self.go_to_add_customer_tab()
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
        self.send_keys(self.LAST_NAME_INPUT, last_name)
        self.send_keys(self.POST_CODE_INPUT, post_code)
        self.click(self.SUBMIT_BTN)

    @allure.step("Получение текста alert")
    def get_alert_text(self) -> str:
        """
        Ожидает появления alert и возвращает его текст.
        """
        alert = self.wait_for_alert(5)
        return alert.text

    @allure.step("Закрытие alert")
    def accept_alert(self) -> None:
        """
        Принимает (закрывает) alert.
        """
        alert = self.wait_for_alert(5)
        alert.accept()

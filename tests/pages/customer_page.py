from selenium.webdriver.common.by import By

from waits import Waits


class CustomersPage:
    CUSTOMERS_BTN = (By.CSS_SELECTOR, 'button[ng-class="btnClass3"]')
    ROWS = (By.CSS_SELECTOR, "table.table-bordered.table-striped tbody tr")
    DELETE_BTN_XPATH = ".//button[contains(text(), 'Delete')]"
    FIRST_NAME_HEADER = (By.XPATH, "//a[contains(text(), 'First Name')]")

    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def go_to_customers_tab(self):
        self.browser.find_element(*self.CUSTOMERS_BTN).click()
        Waits.for_elements(self.browser, self.ROWS, timeout=5)

    def get_first_names(self):
        table_rows = self.browser.find_elements(*self.ROWS)
        first_names = []
        for row in table_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells:
                first_names.append(cells[0].text)
        return first_names

    def sort_by_first_name(self):
        self.browser.find_element(*self.FIRST_NAME_HEADER).click()

    def delete_customer(self, name_to_delete):
        table_rows = self.browser.find_elements(*self.ROWS)
        for row in table_rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if cells and cells[0].text == name_to_delete:
                delete_btn = row.find_element(By.XPATH, self.DELETE_BTN_XPATH)
                delete_btn.click()
                break

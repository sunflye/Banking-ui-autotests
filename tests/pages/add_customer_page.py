from selenium.webdriver.common.by import By

from waits import Waits


class AddCustomerPage:
    ADD_CUSTOMER_BTN = (By.CSS_SELECTOR, 'button[ng-class="btnClass1"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='fName']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input[ng-model='lName']")
    POST_CODE_INPUT = (By.CSS_SELECTOR, "input[ng-model='postCd']")
    SUBMIT_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def go_to_add_customer_tab(self):
        self.browser.find_element(*self.ADD_CUSTOMER_BTN).click()

    def add_customer(self, first_name, last_name, post_code):
        self.go_to_add_customer_tab()
        self.browser.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.browser.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.browser.find_element(*self.POST_CODE_INPUT).send_keys(post_code)
        self.browser.find_element(*self.SUBMIT_BTN).click()
        alert = Waits.for_alert(self.browser, 5)
        assert "Customer added successfully" in alert.text, "Alert text mismatch"
        alert.accept()

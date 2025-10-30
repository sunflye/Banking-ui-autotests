from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class Waits:
    @staticmethod
    def for_alert(browser, timeout=5):
        """
        Ожидает появления alert-окна в браузере.
        """
        WebDriverWait(browser, timeout).until(EC.alert_is_present())
        return Alert(browser)

    @staticmethod
    def for_element(browser, locator, timeout=5):
        """
        Ожидает появления одного элемента на странице.
        """
        return WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @staticmethod
    def for_elements(browser, locator, timeout=5):
        """
        Ожидает появления всех элементов по заданному локатору.
        """
        return WebDriverWait(browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

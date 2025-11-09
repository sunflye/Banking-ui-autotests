from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class BasePage:
    """
    Базовый класс для всех Page Object.
    Содержит общие методы для работы с драйвером, элементами и ожиданиями.
    """

    def __init__(self, browser):
        """
        Инициализация базовой страницы.
        """
        self.browser = browser

    def open(self, url):
        """
        Открывает указанный URL в браузере.
        """
        self.browser.get(url)

    def find_element(self, locator, timeout=5):
        """
        Находит элемент по локатору с ожиданием.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=5):
        """
        Находит все элементы по локатору с ожиданием.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click(self, locator, timeout=5):
        """
        Кликает по элементу, найденному по локатору.
        """
        self.find_element(locator, timeout).click()

    def send_keys(self, locator, value, timeout=5):
        """
        Вводит текст в элемент, найденный по локатору.
        """
        self.find_element(locator, timeout).send_keys(value)

    def find_child_element(self, parent, by, value):
        """
        Находит дочерний элемент внутри родительского.
        """
        return parent.find_element(by, value)

    def find_child_elements(self, parent, by, value):
        """
        Находит все дочерние элементы внутри родительского.
        """
        return parent.find_elements(by, value)

    def wait_for_alert(self, timeout=5):
        """
        Ожидает появления alert-окна и возвращает его.
        """
        WebDriverWait(self.browser, timeout).until(EC.alert_is_present())
        return Alert(self.browser)

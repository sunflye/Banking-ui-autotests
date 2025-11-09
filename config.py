BASE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject"
"""
Базовый URL для приложения.
"""

MANAGER_PATH = "#/manager"
"""
Путь к странице менеджера.
"""

CUSTOMER_PATH = "#/customer"
"""
Путь к странице клиента.
"""


def url(path: str) -> str:
    """
    Формирует полный URL на основе базового адреса и относительного пути.
    """
    return f"{BASE_URL}/{path}"

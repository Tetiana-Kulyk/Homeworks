from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 10, 1)

    __account_button = (By.XPATH, "//a[text() = 'Кабінет']")

    def is_account_button_displayed(self):
        account_button_element = self.__wait.until(EC.visibility_of_element_located(self.__account_button))
        return account_button_element.is_displayed()
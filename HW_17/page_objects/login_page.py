from selenium.webdriver.common.by import By

from page_objects.main_page import DashboardPage
from utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __dropdown_menu = (By.XPATH, "//div[text()[contains(.,'Вхід')]]")
    __email_input = (By.XPATH, "//input[@name= 'user_login']")
    __password_input = (By.XPATH, "//input[@name= 'user_pw']")
    __login_button = (By.XPATH, "//button[text() = 'Увійти']")

    def expand_dropdown_menu(self):
        self._click(self.__dropdown_menu)
        return self

    def set_email(self, email: str):
        self._send_keys(locator=self.__email_input, value=email)
        return self

    def set_password(self, password: str):
        self._send_keys(locator=self.__password_input, value=password)
        return self

    def click_login_button(self):
        self._click(self.__login_button)
        return DashboardPage(self.driver)

    def login(self, email, password):
        self.set_email(email).set_password(password).click_login_button()
        return DashboardPage(self.driver)
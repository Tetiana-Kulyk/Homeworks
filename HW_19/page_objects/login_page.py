from selenium.webdriver.common.by import By
from page_objects.main_page import MainPage
from utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __dropdown_menu = (By.XPATH, "//div[text()[contains(.,'Вхід')]]")
    __dropdown_popup = (By.XPATH, "//form[@data-popup='auth']")
    __email_input = (By.XPATH, "//input[@name= 'user_login']")
    __password_input = (By.XPATH, "//input[@name= 'user_pw']")
    __login_button = (By.XPATH, "//button[text() = 'Увійти']")
    __email_to_subscribe = (By.XPATH, "//input[@placeholder = 'Електронна пошта']")
    __subscribe_button = (By.XPATH, "//button[@class= 'footer-submit']")
    __failed_subscription_popup = (By.XPATH, "//div[text() = 'Ви вже підписані на цю розсилку!']")
    __successful_subscription_popup = (By.XPATH, "//div[text() = 'Ви вдало підписались на цю розсилку! ']")
    __forget_password = (By.XPATH, "//div[@data-popup-handler = 'forget-password']")
    __email_to_remind = (
        By.XPATH, "//form[@data-popup='forget-password']/div/div/div/div/input[@placeholder = 'E-mail']")
    __remind_button = (By.XPATH, "//button[text() = 'Нагадати']")
    __successful_password_reset_popup = (
        By.XPATH, "//div[contains(text(), 'було надіслано посилання для встановлення нового пароля')]")
    __failed_password_reset_popup = (By.XPATH, "//div[text()= 'Користувач не знайдений у базі даних']")

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
        self._is_element_disappeared(locator=self.__dropdown_popup)
        return MainPage(self.driver)

    def login(self, email, password):
        self.set_email(email).set_password(password).click_login_button()
        return MainPage(self.driver)

    def subscribe_with_new_email(self, email):
        self._send_keys(locator=self.__email_to_subscribe, value=email)
        self._click(self.__subscribe_button)
        return self

    def subscribe_with_existing_email(self, email):
        self._send_keys(locator=self.__email_to_subscribe, value=email)
        self._click(self.__subscribe_button)
        return self

    def is_subscription_failed(self):
        return self._is_displayed(locator=self.__failed_subscription_popup)

    def is_subscription_successful(self):
        return self._is_displayed(locator=self.__successful_subscription_popup)

    def remind_password(self, email):
        self._click(self.__forget_password)
        self._send_keys(locator=self.__email_to_remind, value=email)
        self._click(self.__remind_button)
        return self

    def is_password_reset_message_successfully_sent(self):
        return self._is_displayed(locator=self.__successful_password_reset_popup)

    def is_password_reset_message_sending_failed(self):
        return self._is_displayed(locator=self.__failed_password_reset_popup)

    def is_login_button_displayed(self):
        return self._is_displayed(locator=self.__dropdown_menu)

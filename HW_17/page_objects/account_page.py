from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __logout_button = (By.XPATH, "//a[@href='/ua/user/logout/']")
    __login_button = (By.XPATH, "//a[@href='/ua/user/logout/']")
    __account_page = (By.XPATH, "//h1[text() = 'Особистий кабінет']")
    __address_book_button = (By.XPATH, "//li[2][@class='private-office__tabs__item']")
    __wishlist_button = (By.XPATH, "//li[@class='private-office__tabs__item wish-list']")
    __orders_history_button = (By.XPATH, "//li[@class='private-office__tabs__item history-order']")
    __address_book_tab_active = (By.XPATH, "//li[@class='private-office__tabs__item active']")
    __wishlist_tab_active = (By.XPATH, "//li[@class='private-office__tabs__item wish-list active']")
    __orders_history_tab_active = (By.XPATH, "//li[@class='private-office__tabs__item history-order active']")
    __contact_info_tab_active = (By.XPATH, "//li[1][@class='private-office__tabs__item active']")

    def is_account_page_opened(self):
        return self._is_page_opened(locator=self.__account_page)

    def logout(self):
        self._click(self.__logout_button)
        from page_objects.login_page import LoginPage
        return LoginPage(self.driver)

    def open_address_book_tab(self):
        self._click(self.__address_book_button)
        return self

    def is_address_book_tab_active(self):
        return self._is_page_opened(locator=self.__address_book_tab_active)

    def open_wishlist_tab(self):
        self._click(self.__wishlist_button)
        return self

    def is_wishlist_tab_active(self):
        return self._is_page_opened(locator=self.__wishlist_tab_active)

    def open_orders_history_tab(self):
        self._click(self.__orders_history_button)
        return self

    def is_orders_history_tab_active(self):
        return self._is_page_opened(locator=self.__orders_history_tab_active)

    def is_contact_info_page_opened(self):
        return self._is_page_opened(locator=self.__contact_info_tab_active)




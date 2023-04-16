from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage


class WishlistPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __wishlist_tab_active = (By.XPATH, "//li[@class='private-office__tabs__item wish-list active']")
    __monitor_price_checkbox1 = (By.XPATH, "//li/div[2]/div[2]")
    __buy_button = (By.XPATH, "//li[1]/div[2]/div[@class='button buy']")
    __continue_shopping = (By.XPATH, "//div[text()='Продовжити покупки']")
    __notify_about_availability = (By.XPATH, "//li[5]/div[2]/div[1]")
    __selected_price_checkbox = (By.XPATH, "//input[@id='set_price_inform-819358-1903479'][@checked]")
    __selected_availability_checkbox = (By.XPATH, "//input[@id='set_inform-811501-1816960'][@checked]")

    def is_wishlist_page_opened(self):
        return self._is_page_opened(locator=self.__wishlist_tab_active)

    def monitor_price(self):
        self._click(locator=self.__monitor_price_checkbox1)
        return self

    def is_price_checkbox_checked(self):
        if self._is_selected(locator=self.__selected_price_checkbox):
            return True
        else:
            return False

    def notify_about_availability(self):
        self._click(locator=self.__notify_about_availability)
        return self

    def is_notify_about_availability_checkbox_checked(self):
        if self._is_selected(locator=self.__selected_availability_checkbox):
            return True
        else:
            return False

    def click_buy_button(self):
        self._click(locator=self.__buy_button)
        return self

    def continue_shopping(self):
        self._click(locator=self.__continue_shopping)
        return WishlistPage(self.driver)

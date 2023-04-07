from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __hair_page = (By.XPATH, "//li/span[text() = 'Косметика для волосся']")
    __monitor_the_price = (By.XPATH, "//div[3]/div/div/div[2][@class='button apply']")
    __search_field = (By.XPATH, "//input[@id='search-input']")
    __search_button = (By.XPATH, "//form/button[@type='submit']")
    __searched_item = (By.XPATH, "//li/div/a[@href = '/ua/product/182877/']")

    def is_category_page_opened(self):
        return self._is_page_opened(locator=self.__hair_page)

    def search_item(self):
        self._send_keys(locator=self.__search_field, value='Batiste Dry Shampoo Clean and Classic Original')
        self._click(self.__search_button)
        return self

    def is_searched_item_displayed(self):
        searched_item = self._wait_until_element_located(locator=self.__searched_item)
        return searched_item.is_displayed()

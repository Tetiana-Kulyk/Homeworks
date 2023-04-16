from selenium.webdriver.common.by import By
from utilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __account_button = (By.XPATH, "//header/div/div/div/a[@href='/ua/user/']")
    __wishlist_button = (By.XPATH, "//span[@class='favourite-count']")
    __hair_category_button = (By.XPATH, "//ul[@class='menu-list']/li/a[@href = '/ua/categorys/20272/']")
    __promotions_button = (By.XPATH, "//ul/li[1]/a[@class='header-top-list__link']")
    __promotions_page = (By.XPATH, "//h1[text() = 'Акції']")
    __dropdown_menu = (By.XPATH, "//div[text()[contains(.,'Вхід')]]")
    __change_language_button = (By.XPATH, "//a[@lang='ru']")
    __ru_site_lang = (By.XPATH, "//html[@lang='ru']")

    def is_account_button_displayed(self):
        return self._is_page_opened(locator=self.__account_button)

    def click_wishlist_button(self):
        self._click(self.__wishlist_button)
        from page_objects.wishlist_page import WishlistPage
        return WishlistPage(self.driver)

    def click_hair_category_button(self):
        self._click(self.__hair_category_button)
        from page_objects.category_page import CategoryPage
        return CategoryPage(self.driver)

    def click_promotions_button(self):
        self._click(self.__promotions_button)
        return self

    def is_promotions_page_opened(self):
        return self._is_displayed(locator=self.__promotions_page)

    def click_account_button(self):
        self._click(self.__account_button)
        from page_objects.account_page import AccountPage
        return AccountPage(self.driver)

    def change_site_language(self):
        self._click(self.__change_language_button)
        return self

    def is_site_language_ru(self):
        self._wait_until_element_located(locator=self.__ru_site_lang)
        return self._find_in_dom(locator=self.__ru_site_lang)

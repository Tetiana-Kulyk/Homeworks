import pytest
import random
import string
from utilities.config_reader import get_application_url, get_browser_id, get_user_creds
from utilities.driver_factory import driver_factory
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from page_objects.category_page import CategoryPage
from page_objects.account_page import AccountPage
from page_objects.wishlist_page import WishlistPage


@pytest.fixture()
def create_browser():
    driver = driver_factory(get_browser_id())
    driver.maximize_window()
    driver.get(get_application_url())
    yield driver
    driver.quit()


@pytest.fixture()
def generate_random_email():
    random_email = [''.join(random.choice(string.ascii_letters) for _ in range(10))]
    random_email += "@fake.com"
    return random_email


@pytest.fixture()
def open_login_page(create_browser):
    return LoginPage(create_browser)


@pytest.fixture()
def expand_dropdown_menu(open_login_page):
    return open_login_page.expand_dropdown_menu()


@pytest.fixture()
def open_main_page(open_login_page, expand_dropdown_menu):
    return expand_dropdown_menu.login(get_user_creds()[0], get_user_creds()[1])


@pytest.fixture()
def open_wishlist_page(open_main_page, create_browser):
    return MainPage(create_browser).click_wishlist_button()


@pytest.fixture()
def open_hair_category_page(open_main_page, create_browser):
    return MainPage(create_browser).click_hair_category_button()


@pytest.fixture()
def open_promotions_page(open_main_page, create_browser):
    return MainPage(create_browser).click_promotions_button()


@pytest.fixture()
def logout(open_main_page, create_browser):
    return MainPage(create_browser).click_account_button().logout()


@pytest.fixture()
def open_account_page(open_main_page, create_browser):
    return MainPage(create_browser).click_account_button()


@pytest.fixture
def open_address_book_tab(open_account_page, create_browser):
    return AccountPage(create_browser).open_address_book_tab()


@pytest.fixture
def open_wishlist_tab(open_account_page, create_browser):
    return AccountPage(create_browser).open_wishlist_tab()


@pytest.fixture
def open_orders_history_tab(open_account_page, create_browser):
    return AccountPage(create_browser).open_orders_history_tab()


@pytest.fixture
def change_site_language(open_main_page, create_browser):
    return MainPage(create_browser).change_site_language()


@pytest.fixture
def check_monitor_price(open_wishlist_page, create_browser):
    return WishlistPage(create_browser).monitor_price()


@pytest.fixture
def notify_about_availability(open_wishlist_page, create_browser):
    return WishlistPage(create_browser).notify_about_availability()


@pytest.fixture
def search_item(open_hair_category_page, create_browser):
    return CategoryPage(create_browser).search_item()


@pytest.fixture
def add_to_basket_from_wishlist(open_wishlist_page, create_browser):
    from page_objects.wishlist_page import WishlistPage
    return WishlistPage(create_browser).click_buy_button().continue_shopping()

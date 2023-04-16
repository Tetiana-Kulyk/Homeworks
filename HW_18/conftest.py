import json
import pytest
import random
import string
from constants import ROOT_DIR
from utilities.driver_factory import driver_factory
from page_objects.login_page import LoginPage
from utilities.configuration import Configuration


def pytest_addoption(parser):
    parser.addoption('--browser_id', action='store', default=1, help='Set browser id')
    parser.addoption('--env', action='store', help='Env name')


@pytest.fixture(scope='session', autouse=True)
def env():
    with open(f'{ROOT_DIR}/configurations/config.json', 'r') as file:
        res = file.read()
    config = json.loads(res)
    return Configuration(**config)


@pytest.fixture()
def create_browser(env):
    driver = driver_factory(int(env.browser_id))
    driver.maximize_window()
    driver.get(env.app_url)
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
def open_main_page(open_login_page, expand_dropdown_menu, env):
    return expand_dropdown_menu.login(env.email, env.password)


@pytest.fixture()
def open_wishlist_page(open_main_page, create_browser):
    return open_main_page.click_wishlist_button()


@pytest.fixture()
def open_hair_category_page(open_main_page, create_browser):
    return open_main_page.click_hair_category_button()


@pytest.fixture()
def open_promotions_page(open_main_page, create_browser):
    return open_main_page.click_promotions_button()


@pytest.fixture()
def logout(open_main_page, create_browser):
    return open_main_page.click_account_button().logout()


@pytest.fixture()
def open_account_page(open_main_page, create_browser):
    return open_main_page.click_account_button()


@pytest.fixture
def open_address_book_tab(open_account_page, create_browser):
    return open_account_page.open_address_book_tab()


@pytest.fixture
def open_wishlist_tab(open_account_page, create_browser):
    return open_account_page.open_wishlist_tab()


@pytest.fixture
def open_orders_history_tab(open_account_page, create_browser):
    return open_account_page.open_orders_history_tab()


@pytest.fixture
def change_site_language(open_main_page, create_browser):
    return open_main_page.change_site_language()


@pytest.fixture
def check_monitor_price(open_wishlist_page, create_browser):
    return open_wishlist_page.monitor_price()


@pytest.fixture
def notify_about_availability(open_wishlist_page, create_browser):
    return open_wishlist_page.notify_about_availability()


@pytest.fixture
def search_item(open_hair_category_page, create_browser):
    return open_hair_category_page.search_item()


@pytest.fixture
def add_to_basket_from_wishlist(open_wishlist_page, create_browser):
    return open_wishlist_page.click_buy_button().continue_shopping()

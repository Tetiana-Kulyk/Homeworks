import pytest

from utilities.config_reader import get_user_creds


@pytest.mark.login
@pytest.mark.smoke
def test_login(expand_dropdown_menu):
    main_page = expand_dropdown_menu.set_email(get_user_creds()[0]).set_password(
        get_user_creds()[1]).click_login_button()
    assert main_page.is_account_button_displayed(), 'Account button is not displayed'


@pytest.mark.login
@pytest.mark.regression
def test_subscribe_with_existing_email(open_login_page):
    login_page = open_login_page.subscribe_with_existing_email(email=get_user_creds()[0])
    assert login_page.is_subscription_failed(), 'User is able to subscribe with already subscribed email'


@pytest.mark.login
@pytest.mark.regression
def test_subscribe_with_new_email(open_login_page, generate_random_email):
    login_page = open_login_page.subscribe_with_new_email(email=generate_random_email)
    assert login_page.is_subscription_successful(), 'User is not able to subscribe with new email'


@pytest.mark.login
@pytest.mark.regression
def test_password_reset_with_valid_email(expand_dropdown_menu):
    dropdown_menu = expand_dropdown_menu.remind_password(email=get_user_creds()[0])
    assert dropdown_menu.is_password_reset_message_successfully_sent(), 'Password reset message is not sent'


@pytest.mark.login
@pytest.mark.regression
def test_password_reset_with_invalid_email(expand_dropdown_menu, generate_random_email):
    dropdown_menu = expand_dropdown_menu.remind_password(email=generate_random_email)
    assert dropdown_menu.is_password_reset_message_sending_failed(), 'Password reset message is sent to not ' \
                                                                     'registered email'


@pytest.mark.main
@pytest.mark.regression
def test_change_site_language(change_site_language):
    assert change_site_language.is_site_language_ru(), 'Site language is not changed'


@pytest.mark.main
@pytest.mark.smoke
def test_open_hair_category_page(open_hair_category_page):
    assert open_hair_category_page.is_category_page_opened(), 'Hair category page is not opened'


@pytest.mark.main
@pytest.mark.smoke
def test_open_promotions_page(open_promotions_page):
    assert open_promotions_page.is_promotions_page_opened(), 'Promotions page is not opened'


@pytest.mark.main
@pytest.mark.smoke
def test_open_account_page(open_account_page):
    assert open_account_page.is_account_page_opened(), 'Account page is not opened'


@pytest.mark.account
@pytest.mark.smoke
def test_logout(logout):
    assert logout.is_login_button_displayed(), 'Logout is not performed'


@pytest.mark.account
@pytest.mark.smoke
def test_open_contact_info_page(open_account_page):
    open_account_page.is_contact_info_page_opened(), 'Contact info page is not opened'


@pytest.mark.account
@pytest.mark.smoke
def test_open_address_book_tab(open_address_book_tab):
    assert open_address_book_tab.is_address_book_tab_active(), 'Address book tab is not opened'


@pytest.mark.account
@pytest.mark.smoke
def test_open_wishlist_tab(open_wishlist_tab):
    assert open_wishlist_tab.is_wishlist_tab_active(), 'Wishlist tab is not opened'


@pytest.mark.account
@pytest.mark.smoke
def test_open_orders_history_tab(open_orders_history_tab):
    assert open_orders_history_tab.is_orders_history_tab_active(), 'Orders history tab is not opened'


@pytest.mark.account
@pytest.mark.smoke
def test_open_wishlist(open_wishlist_page):
    assert open_wishlist_page.is_wishlist_page_opened(), 'Wishlist page is not opened'


@pytest.mark.regression
def test_search_item(open_hair_category_page):
    assert open_hair_category_page.search_item().is_searched_item_displayed(), "Searched item is not shown in results"


@pytest.mark.regression
@pytest.mark.wishlist
def test_check_monitor_price_checkbox(check_monitor_price):
    assert check_monitor_price.is_price_checkbox_checked(), 'The "monitor price" checkbox is not checked'


@pytest.mark.regression
@pytest.mark.wishlist
def test_notify_about_availability(notify_about_availability):
    assert notify_about_availability.is_notify_about_availability_checkbox_checked(), 'The "notify about ' \
                                                                                      'availability" checkbox is ' \
                                                                                      'not unchecked'


@pytest.mark.regression
@pytest.mark.wishlist
def test_add_to_basket_and_continue_shopping(add_to_basket_from_wishlist):
    assert add_to_basket_from_wishlist.is_wishlist_page_opened(), 'Wishlist page is not opened'

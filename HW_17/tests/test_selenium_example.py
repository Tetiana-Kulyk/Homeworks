from utilities.config_reader import get_user_creds


def test_login(open_login_page, expand_dropdown_menu):
    main_page = expand_dropdown_menu.set_email(get_user_creds()[0]).set_password(get_user_creds()[1]).click_login_button()
    assert main_page.is_account_button_displayed(), 'Account button is not displayed'
import time

from page_objects.register_page import RegisterPage
from page_objects.account_success_page import AccountSuccessPage


def test_register_form(driver, base_url):
    register_page = RegisterPage(driver)
    register_page.open(base_url, '/index.php?route=account/register')

    assert register_page.header_is_visible()
    assert register_page.first_name_input_is_visible()
    assert register_page.last_name_input_is_visible()
    assert register_page.email_input_is_visible()
    assert register_page.telephone_input_is_visible()
    assert register_page.password_input_is_visible()
    assert register_page.confirm_input_is_visible()
    assert register_page.policy_checkbox_is_visible()
    assert register_page.submit_button_is_visible()


def test_register_new_client(driver, base_url, random_email):
    register_page = RegisterPage(driver)
    account_success_page = AccountSuccessPage(driver)
    random_email = random_email

    register_page.open(base_url, '/index.php?route=account/register')

    register_page.input_client_data_to_required_field(first_name='Oksana',
                                                      last_name='Gavrilova',
                                                      email=random_email,
                                                      telephone='89301512526',
                                                      password='12345678')
    register_page.check_policy_checkbox()
    register_page.click_submit_button()

    assert account_success_page.success_header_is_visible()
    assert account_success_page.get_header_text() == 'Your Account Has Been Created!'





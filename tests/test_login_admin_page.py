import pytest
import allure

from page_objects.login_admin_page import LoginAdminPage
from page_objects.admin_home_page import AdminHomePage


@pytest.mark.nondestructive
@pytest.mark.test
@allure.title("")
def test_login_form(driver, base_url):
    login_admin_page = LoginAdminPage(driver)
    login_admin_page.open(base_url, "/administration")

    assert login_admin_page.title_is_visible()
    assert login_admin_page.username_title_is_visible()
    assert login_admin_page.username_field_is_visible()
    assert login_admin_page.password_title_is_visible()
    assert login_admin_page.password_field_is_visible()
    assert login_admin_page.login_button_is_visible()


@pytest.mark.nondestructive
@allure.title("Проверка входа \ выхода")
def test_login_logout(driver, base_url):
    login_admin_page = LoginAdminPage(driver)
    admin_home_page = AdminHomePage(driver)

    login_admin_page.open(base_url, "/administration")
    login_admin_page.login_with_admin_creads(login="user", password="bitnami")

    assert admin_home_page.user_profile_is_visible()

    admin_home_page.click_logout_button()

    assert login_admin_page.login_button_is_visible()

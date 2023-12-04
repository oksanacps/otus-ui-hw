from page_objects.login_admin_page import LoginAdminPage
from page_objects.admin_home_page import AdminHomePage


def test_login_form(driver, base_url):
    login_admin_page = LoginAdminPage(driver)
    login_admin_page.open(base_url, '/admin')

    assert login_admin_page.title_is_visible()
    assert login_admin_page.username_title_is_visible()
    assert login_admin_page.username_field_is_visible()
    assert login_admin_page.password_title_is_visible()
    assert login_admin_page.password_field_is_visible()
    assert login_admin_page.login_button_is_visible()


def test_login_logout(driver, base_url):
    login_admin_page = LoginAdminPage(driver)
    admin_home_page = AdminHomePage(driver)

    login_admin_page.open(base_url, '/admin')
    login_admin_page.login_with_admin_creads(login='user', password='bitnami')

    assert admin_home_page.user_profile_is_visible()

    admin_home_page.click_logout_button()

    assert login_admin_page.login_button_is_visible()

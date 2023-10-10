from pages.pages import LoginAdminPage, AdminHomePage


def test_login_form(driver, base_url):
    browser = driver
    browser.get(base_url + '/admin')

    assert browser.find_element(*LoginAdminPage.TITLE)
    assert browser.find_element(*LoginAdminPage.USERNAME_TITLE)
    assert browser.find_element(*LoginAdminPage.USERNAME_FIELD)
    assert browser.find_element(*LoginAdminPage.PASSWORD_TITLE)
    assert browser.find_element(*LoginAdminPage.PASSWORD_FIELD)
    assert browser.find_element(*LoginAdminPage.LOGIN_BUTTON)


def test_login_logout(driver, base_url):
    browser = driver
    browser.get(base_url + '/admin')
    browser.find_element(*LoginAdminPage.USERNAME_FIELD).send_keys('user')
    browser.find_element(*LoginAdminPage.PASSWORD_FIELD).send_keys('bitnami')
    browser.find_element(*LoginAdminPage.LOGIN_BUTTON).click()

    assert browser.find_element(*AdminHomePage.USER_PROFILE)

    browser.find_element(*AdminHomePage.LOGOUT_BUTTON).click()

    assert browser.find_element(*LoginAdminPage.LOGIN_BUTTON)

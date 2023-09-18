from pages.pages import LoginPage


def test_login(driver, base_url, logout):
    browser = driver
    browser.get(base_url + '/index.php?route=account/login')
    browser.find_element(*LoginPage.EMAIL).send_keys('Ksundeli76@gmail.com')
    browser.find_element(*LoginPage.PASSWORD).send_keys('12345678')
    browser.find_element(*LoginPage.SUBMIT_BUTTON).click()

    assert browser.find_element(*LoginPage.MY_ACCOUNT_HEADER)

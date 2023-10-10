from pages.pages import RegisterPage


def test_register_form(driver, base_url):
    browser = driver
    browser.get(base_url + '/index.php?route=account/register')

    assert browser.find_element(*RegisterPage.HEADER)
    assert browser.find_element(*RegisterPage.FIRST_NAME_INPUT)
    assert browser.find_element(*RegisterPage.LAST_NAME_INPUT)
    assert browser.find_element(*RegisterPage.EMAIL_INPUT)
    assert browser.find_element(*RegisterPage.TELEPHONE_INPUT)
    assert browser.find_element(*RegisterPage.PASSWORD_INPUT)
    assert browser.find_element(*RegisterPage.CONFIRM_INPUT)
    assert browser.find_element(*RegisterPage.POLICY_CHECKBOX)
    assert browser.find_element(*RegisterPage.SUBMIT_BUTTON)

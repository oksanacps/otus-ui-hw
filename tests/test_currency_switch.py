from pages.pages import HomePage, CatalogPage


def test_currency_home_page(driver, base_url):
    browser = driver
    browser.get(base_url)

    browser.find_element(*HomePage.CURRENCY_DROP_DOWN).click()
    browser.find_element(*HomePage.EURO).click()

    assert '€' in browser.find_element(*HomePage.PRICE).text

    browser.find_element(*HomePage.CURRENCY_DROP_DOWN).click()
    browser.find_element(*HomePage.POUND).click()

    assert '£' in browser.find_element(*HomePage.PRICE).text

    browser.find_element(*HomePage.CURRENCY_DROP_DOWN).click()
    browser.find_element(*HomePage.USD).click()

    assert '$' in browser.find_element(*HomePage.PRICE).text


def test_currency_catalog_page(driver, base_url):
    browser = driver
    browser.get(base_url + '/desktops/mac')

    browser.find_element(*HomePage.CURRENCY_DROP_DOWN).click()
    browser.find_element(*HomePage.EURO).click()

    assert '€' in browser.find_element(*CatalogPage.PRICE).text

    browser.find_element(*HomePage.CURRENCY_DROP_DOWN).click()
    browser.find_element(*HomePage.POUND).click()

    assert '£' in browser.find_element(*CatalogPage.PRICE).text

    browser.find_element(*HomePage.CURRENCY_DROP_DOWN).click()
    browser.find_element(*HomePage.USD).click()

    assert '$' in browser.find_element(*CatalogPage.PRICE).text

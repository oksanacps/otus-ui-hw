import pytest

from pages.pages import HomePage, CatalogPage


@pytest.mark.parametrize('currency, expected_icon', [(HomePage.EURO, '€'),
                                                     (HomePage.POUND, '£'),
                                                     (HomePage.USD, '$')
                                                     ])
def test_currency_home_page(driver, base_url, currency, expected_icon):
    browser = driver
    browser.get(base_url)

    browser.find_element(*HomePage.CURRENCY_DROP_DOWN).click()
    browser.find_element(*currency).click()

    assert expected_icon in browser.find_element(*HomePage.PRICE).text


@pytest.mark.parametrize('currency, expected_icon', [(HomePage.EURO, '€'),
                                                     (HomePage.POUND, '£'),
                                                     (HomePage.USD, '$')
                                                     ])
def test_currency_catalog_page(driver, base_url, currency, expected_icon):
    browser = driver
    browser.get(base_url + '/desktops/mac')

    browser.find_element(*HomePage.CURRENCY_DROP_DOWN).click()
    browser.find_element(*currency).click()

    assert expected_icon in browser.find_element(*CatalogPage.PRICE).text

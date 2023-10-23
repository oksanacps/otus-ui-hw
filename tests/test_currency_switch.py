import pytest

from page_objects.home_page import HomePage
from page_objects.catalog_page import CatalogPage


@pytest.mark.parametrize('currency, expected_icon', [('EURO', '€'),
                                                     ('POUND', '£'),
                                                     ('USD', '$')
                                                     ])
def test_currency_home_page(driver, base_url, currency, expected_icon):
    home_page = HomePage(driver)
    home_page.open(base_url)

    home_page.click_currency_drop_down()
    home_page.click_on_currency_icon()

    assert expected_icon in home_page.get_price()


@pytest.mark.parametrize('currency, expected_icon', [('EURO', '€'.encode("utf-8")),
                                                     ('POUND', '£'.encode("utf-8")),
                                                     ('USD', '$'.encode("utf-8"))    # почему тут ошибка кодировки?
                                                     ])
def test_currency_catalog_page(driver, base_url, currency, expected_icon):
    catalog_page = CatalogPage(driver)
    home_page = HomePage(driver)
    catalog_page.open(base_url, '/desktops/mac')

    home_page.click_currency_drop_down()
    home_page.click_on_currency_icon(currency)

    assert expected_icon in catalog_page.get_price()

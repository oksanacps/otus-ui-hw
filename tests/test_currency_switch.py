import pytest
import allure

from page_objects.home_page import HomePage
from page_objects.catalog_page import CatalogPage


@pytest.mark.skip(reason="Тест падает из-за кодировки")
@pytest.mark.nondestructive
@pytest.mark.parametrize(
    "currency, expected_icon",
    [("EURO", "€"), ("POUND", "£"), ("USD", "$")],
    ids=["Евро", "Фунты", "Доллары"],
)
@allure.title("Проверка выбора валюты на главной странице")
def test_currency_home_page(driver, base_url, currency, expected_icon):
    home_page = HomePage(driver)
    home_page.open(base_url)

    home_page.click_currency_drop_down()
    home_page.click_on_currency_icon(currency)

    assert expected_icon in home_page.get_price()


@pytest.mark.skip(reason="Тест падает из-за кодировки")
@pytest.mark.nondestructive
@pytest.mark.parametrize(
    "currency, expected_icon",
    [("EURO", "€"), ("POUND", "£"), ("USD", "$")],
    ids=["Евро", "Фунты", "Доллары"],
)
@allure.title("Проверка выбора валюты на странице с каталогом товаров")
def test_currency_catalog_page(driver, base_url, currency, expected_icon):
    catalog_page = CatalogPage(driver)
    home_page = HomePage(driver)
    catalog_page.open(base_url, "/desktops/mac")

    home_page.click_currency_drop_down()
    home_page.click_on_currency_icon(currency)

    assert expected_icon in catalog_page.get_price()

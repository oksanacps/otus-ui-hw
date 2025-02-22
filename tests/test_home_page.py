import pytest

from page_objects.home_page import HomePage

@pytest.mark.nondestructive
def test_home_page(driver, base_url):
    home_page = HomePage(driver)
    home_page.open(base_url)

    assert home_page.logo_is_visible()
    assert home_page.search_field_is_visible()
    assert home_page.cart_is_visible()

    assert home_page.number_of_products() > 0

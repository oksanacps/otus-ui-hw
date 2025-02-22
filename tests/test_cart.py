import pytest

from page_objects.home_page import HomePage

@pytest.mark.nondestructive
def test_add_product_to_cart(driver, base_url, clear_cart):
    home_page = HomePage(driver)
    home_page.open(base_url)

    home_page.click_cart_button()
    home_page.close_alert()
    home_page.click_cart()
    products_in_cart = home_page.number_of_products_in_cart()

    assert products_in_cart == 1

from page_objects.home_page import HomePage
from page_objects.mac_page import MacPage
from page_objects.search_page import SearchPage
from page_objects.contact_page import ContactPage


def test_find_search_field(driver, base_url):
    home_page = HomePage(driver)
    home_page.open(base_url)
    assert home_page.search_field_is_visible()


def test_find_shopping_cart_on_mac(driver, base_url):
    mac_page = MacPage(driver)
    mac_page.open(base_url, "/desktops/mac")
    assert mac_page.shoping_cart_mac_is_visible()


def test_find_contact_form(driver, base_url):
    contact_page = ContactPage(driver)
    contact_page.open(base_url, "/en-gb?route=information/contact")
    assert contact_page.contact_form_is_visible()
    assert contact_page.lable_contact_form_is_visible()


def test_find_button_search(driver, base_url):
    search_page = SearchPage(driver)
    search_page.open(base_url, "/index.php?route=product/search")
    assert search_page.button_search_is_visible()

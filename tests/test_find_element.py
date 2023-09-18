from pages.pages import MacPage, SearchPage, HomePage, ContactPage


def test_find_search_field(driver, base_url):
    browser = driver
    browser.get(base_url)
    assert browser.find_element(*HomePage.SEARCH_FIELD)


def test_find_shopping_cart_on_mac(driver, base_url):
    browser = driver
    browser.get(base_url + '/desktops/mac')
    assert browser.find_element(*MacPage.SHOPPING_CART_MAC)  #by.css


def test_find_all_categories_on_menu(driver, base_url):
    browser = driver
    browser.get(base_url)
    categories = browser.find_elements(*HomePage.CATEGORIES)
    assert len(categories) == 8


def test_find_contact_form(driver, base_url):
    browser = driver
    browser.get(base_url + '/index.php?route=information/contact')
    assert browser.find_element(*ContactPage.CONTACT_FORM)
    assert browser.find_element(*ContactPage.LABLE_CONTACT_FORM)


def test_find_button_search(driver, base_url):
    browser = driver
    browser.get(base_url + '/index.php?route=product/search')
    assert browser.find_element(*SearchPage.BUTTON_SEARCH)

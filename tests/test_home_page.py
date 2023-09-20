from pages.pages import HomePage


def test_home_page(driver, base_url):
    browser = driver
    browser.get(base_url)

    assert browser.find_element(*HomePage.LOGO)
    assert browser.find_element(*HomePage.SEARCH_FIELD)
    assert browser.find_element(*HomePage.CART)
    assert len(browser.find_elements(*HomePage.CATEGORIES)) > 0
    assert len(browser.find_elements(*HomePage.PRODUCTS)) > 0

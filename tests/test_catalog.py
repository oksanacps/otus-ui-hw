from pages.pages import CatalogPage


def test_catalog_page(driver, base_url):
    browser = driver
    browser.get(base_url + '/component/monitor')

    assert browser.find_element(*CatalogPage.BREADCRUMBS)
    assert browser.find_element(*CatalogPage.CATALOG_HEADER)
    assert len(browser.find_elements(*CatalogPage.PRODUCTS)) > 0
    assert browser.find_element(*CatalogPage.CART_BUTTON)
    assert browser.find_element(*CatalogPage.PRODUCT_HEADER)

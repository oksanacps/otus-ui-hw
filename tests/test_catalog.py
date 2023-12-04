from page_objects.catalog_page import CatalogPage


def test_catalog_page(driver, base_url):
    catalog_page = CatalogPage(driver)
    catalog_page.open(base_url, catalog_page.PATH)

    assert catalog_page.breadcrumbs_is_visible()
    assert catalog_page.catalog_header_is_visible()
    assert catalog_page.number_of_products() > 0
    assert catalog_page.cart_button_is_visible()
    assert catalog_page.product_header()

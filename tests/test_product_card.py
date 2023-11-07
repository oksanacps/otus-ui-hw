from page_objects.product_card_page import ProductCardPage


def test_desctop_mac_card(driver, base_url):
    product_card_page = ProductCardPage(driver)
    product_card_page.open(base_url, '/desktops/mac/imac')

    assert product_card_page.images_number() > 0
    assert product_card_page.product_name_is_visible()
    assert product_card_page.price_is_visible()
    assert product_card_page.add_cart_button_is_visible()
    assert product_card_page.description_is_visible()
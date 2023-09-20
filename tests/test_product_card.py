from pages.pages import ProductCardPage


def test_desctop_mac_card(driver, base_url):
    browser = driver
    browser.get(base_url + '/desktops/mac/imac')

    assert len(browser.find_elements(*ProductCardPage.IMAGES)) > 0
    assert browser.find_element(*ProductCardPage.PRODUCT_NAME)
    assert browser.find_element(*ProductCardPage.PRICE)
    assert browser.find_element(*ProductCardPage.ADD_CART_BUTTON)
    assert browser.find_element(*ProductCardPage.DESCRIPTION)

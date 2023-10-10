from selenium.webdriver.common.by import By

from pages.pages import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_product_to_cart(driver, base_url, clear_cart):
    browser = driver
    browser.get(base_url)

    browser.find_element(*HomePage.CART_BUTTON).click()
    browser.find_element(*HomePage.CART).click()
    products_in_cart = WebDriverWait(browser, 2).until(
        EC.visibility_of_all_elements_located((
            By.CSS_SELECTOR, '[class="table table-striped"] > tbody > tr'
        )))

    assert len(products_in_cart) == 1

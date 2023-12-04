from selenium.webdriver.common.by import By

from page_objects.home_page import HomePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_product_to_cart(driver, base_url, clear_cart):
    home_page = HomePage(driver)
    home_page.open(base_url)

    home_page.click_cart_button()
    home_page.click_cart()
    products_in_cart = WebDriverWait(driver, 5).until(
        EC.visibility_of_all_elements_located((
            By.CSS_SELECTOR, '[class="table table-striped"] > tbody > tr'
        )))

    assert len(products_in_cart) == 1

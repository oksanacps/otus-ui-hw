from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductCardPage(BasePage):
    PATH = "/en-gb/product/desktops/mac/imac"

    def images_number(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, ".thumbnails > li"))

    def product_name_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm > h1")
        return True

    def price_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm .price-new")
        return True

    def add_cart_button_is_visible(self):
        self.driver.find_element(By.ID, "button-cart")
        return True

    def description_is_visible(self):
        self.driver.find_element(By.ID, "tab-description")
        return True

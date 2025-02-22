from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    PATH = '/en-gb/catalog/component/monitor'

    def breadcrumbs_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.breadcrumb')
        return True

    def catalog_header_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '#content > h2')
        return True

    def number_of_products(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, '.product-thumb'))

    def cart_button_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Add to Cart"]')
        return True

    def product_header(self):
        self.driver.find_element(By.CSS_SELECTOR, '.description > h4')
        return True

    def get_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.price').text

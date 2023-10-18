from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def search_field_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '#search')
        return True

    def number_of_categories(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, "[class='nav navbar-nav'] > li"))

    def logo_is_visible(self):
        self.driver.find_element(By.ID, 'logo')
        return True

    def cart_is_visible(self):
        self.driver.find_element(By.ID, 'cart')
        return True

    def number_of_products(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, '.row > div > [class="product-thumb transition"]'))

    def cart_button_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.button-group > [type="button"] > [class="fa fa-shopping-cart"]')

    def products_in_cart_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="table table-striped"] > tbody > tr')

    def currency_drop_down_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa fa-caret-down"]')

    def euro_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '[name="EUR"]')

    def pound_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '[name="GBP"]')

    def usd_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '[name="GBP"]')

    def price_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.price-new')

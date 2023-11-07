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

    def click_cart(self):
        self.driver.find_element(By.ID, 'cart').click()

    def number_of_products(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, '.row > div > [class="product-thumb transition"]'))

    def click_cart_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '.button-group > [type="button"] > [class="fa fa-shopping-cart"]').click()

    def number_of_products_in_cart(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, '[class="table table-striped"] > tbody > tr'))

    def click_currency_drop_down(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa fa-caret-down"]').click()

    def get_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.price-new').text

    def click_on_currency_icon(self, currency):
        if currency == 'EURO':
            self.driver.find_element(By.CSS_SELECTOR, '[name="EUR"]').click()
        elif currency == 'POUND':
            self.driver.find_element(By.CSS_SELECTOR, '[name="GBP"]').click()
        elif currency == 'USD':
            self.driver.find_element(By.CSS_SELECTOR, '[name="USD"]').click()



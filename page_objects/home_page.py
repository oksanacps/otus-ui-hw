from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    def search_field_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '#search')
        return True

    def logo_is_visible(self):
        self.driver.find_element(By.ID, 'logo')
        return True

    def cart_is_visible(self):
        self.driver.find_element(By.ID, 'header-cart')
        return True

    def click_cart(self):
        cart = self.driver.find_element(By.CSS_SELECTOR, '#header-cart')
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cart)
        cart.click()

    def number_of_products(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, '.product-thumb'))

    def click_cart_button(self):
        cart_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"][formaction="http://192.168.0.102:8081/en-gb?route=checkout/cart.add"]')
        self.driver.execute_script("arguments[0].click();", cart_button)

    def number_of_products_in_cart(self):
        if len(self.driver.find_elements(By.CSS_SELECTOR, 'li.text-center.p-4')) == 1:
            return 0
        else:
            number_of_products_in_cart = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located((
                By.XPATH, '//*[@id="header-cart"]/div/ul/li/table/tbody/tr'
            )))
            return len(number_of_products_in_cart)

    def click_currency_drop_down(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa-solid fa-caret-down"]').click()

    def get_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.price-new').text

    def click_on_currency_icon(self, currency):
        if currency == 'EURO':
            self.driver.find_element(By.CSS_SELECTOR, '[href="EUR"]').click()
        elif currency == 'POUND':
            self.driver.find_element(By.CSS_SELECTOR, '[href="GBP"]').click()
        elif currency == 'USD':
            self.driver.find_element(By.CSS_SELECTOR, '[href="USD"]').click()

    def close_alert(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#alert')))
        close_alert = self.driver.find_element(By.CSS_SELECTOR, 'btn-close')
        close_alert.click()

import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    @allure.step("Проверяю, что поле поиска отображается")
    def search_field_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#search")
        return True

    @allure.step("Проверяю, что логотип отображается")
    def logo_is_visible(self):
        self.driver.find_element(By.ID, "logo")
        return True

    @allure.step("Проверяю, что корзина отображается")
    def cart_is_visible(self):
        self.driver.find_element(By.ID, "header-cart")
        return True

    @allure.step("Нажимаю на кнопку 'Корзина' в заголовке")
    def click_cart(self):
        cart = self.driver.find_element(By.CSS_SELECTOR, "#header-cart")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cart)
        cart.click()

    @allure.step("Получаю кол-во товаров на странице")
    def number_of_products(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, ".product-thumb"))

    @allure.step("Нажимаю на кнопку 'Корзина' в карточке товара")
    def click_cart_button(self):
        cart_button = self.driver.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"][formaction="http://192.168.0.102:8081/en-gb?route=checkout/cart.add"]',
        )
        self.driver.execute_script("arguments[0].click();", cart_button)

    @allure.step("Получаю, кол-во товаров в корзине")
    def number_of_products_in_cart(self):
        if len(self.driver.find_elements(By.CSS_SELECTOR, "li.text-center.p-4")) == 1:
            return 0
        else:
            number_of_products_in_cart = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_all_elements_located(
                    (By.XPATH, '//*[@id="header-cart"]/div/ul/li/table/tbody/tr')
                )
            )
            return len(number_of_products_in_cart)

    @allure.step("Нажимаю на кнопку выбора валюты")
    def click_currency_drop_down(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '[class="fa-solid fa-caret-down"]'
        ).click()

    @allure.step("Получаю цену в карточке товара")
    def get_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".price-new").text

    @allure.step("Нажимаю на иконку с валютой")
    def click_on_currency_icon(self, currency):
        if currency == "EURO":
            self.driver.find_element(By.CSS_SELECTOR, '[href="EUR"]').click()
        elif currency == "POUND":
            self.driver.find_element(By.CSS_SELECTOR, '[href="GBP"]').click()
        elif currency == "USD":
            self.driver.find_element(By.CSS_SELECTOR, '[href="USD"]').click()

    @allure.step("Закрываю информационное всплывающее окно")
    def close_alert(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#alert"))
        )
        close_alert = self.driver.find_element(By.CSS_SELECTOR, "btn-close")
        close_alert.click()

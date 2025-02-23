import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    PATH = "/en-gb/catalog/component/monitor"

    @allure.step("Проверяю, что breadcrumbs отображается")
    def breadcrumbs_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, ".breadcrumb")
        return True

    @allure.step("Проверяю, что заголовок каталога отображается")
    def catalog_header_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#content > h2")
        return True

    @allure.step("Получаю кол-во товаров")
    def number_of_products(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, ".product-thumb"))

    @allure.step("Проверяю, что кнопка добавления в корзину отображается")
    def cart_button_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Add to Cart"]')
        return True

    @allure.step("Проверяю, что заголовок товара отображается")
    def product_header(self):
        self.driver.find_element(By.CSS_SELECTOR, ".description > h4")
        return True

    @allure.step("Получаю цену товара на карточке")
    def get_price(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".price").text

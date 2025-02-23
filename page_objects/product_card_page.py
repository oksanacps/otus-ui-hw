import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


@allure.step("")
class ProductCardPage(BasePage):
    PATH = "/en-gb/product/desktops/mac/imac"

    @allure.step("Получаю кол-во изображений товара")
    def images_number(self):
        return len(self.driver.find_elements(By.CSS_SELECTOR, ".thumbnails > li"))

    @allure.step("Проверяю, что наименование товара отображается")
    def product_name_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm > h1")
        return True

    @allure.step("Проверяю, что цена товара отображается")
    def price_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm .price-new")
        return True

    @allure.step("Проверяю, что кнопка добавления товара в корзину отображается")
    def add_cart_button_is_visible(self):
        self.driver.find_element(By.ID, "button-cart")
        return True

    @allure.step("Проверяю, что описание отображается")
    def description_is_visible(self):
        self.driver.find_element(By.ID, "tab-description")
        return True

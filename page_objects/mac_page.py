import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class MacPage(BasePage):
    PATH = "/en-gb/catalog/desktops/mac"

    @allure.step("Проверяю, что карточка с товаром mac отображается")
    def shoping_cart_mac_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, ".button-group > button:nth-child(1)")
        return True

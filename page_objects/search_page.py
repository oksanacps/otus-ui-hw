import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    PATH = "/en-gb?route=product/search"

    @allure.step("Проверяю, что кнопка поиска отображается")
    def button_search_is_visible(self):
        self.driver.find_element(By.ID, "button-search")
        return True

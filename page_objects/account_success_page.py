import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountSuccessPage(BasePage):
    PATH = ""

    @allure.step("Проверяю, что заголовок отображается")
    def success_header_is_visible(self):
        return self.is_visible((By.CSS_SELECTOR, "#content > h1"))

    @allure.step("Получаю текст в заголовке")
    def get_header_text(self):
        return self.get_text(By.CSS_SELECTOR, "#content > h1")

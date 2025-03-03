import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminHomePage(BasePage):
    PATH = ""

    @allure.step("Проверяю, что пользовательский профиль отображается")
    def user_profile_is_visible(self):
        return self.is_visible((By.CSS_SELECTOR, "#nav-profile"))

    @allure.step("Нажимаю logout кнопку")
    def click_logout_button(self):
        self.click((By.CSS_SELECTOR, "#nav-logout"))

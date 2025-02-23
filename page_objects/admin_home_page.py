import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminHomePage(BasePage):
    PATH = ""

    @allure.step("Проверяю, что пользовательский профиль отображается")
    def user_profile_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#nav-profile")
        return True

    @allure.step("Нажимаю logout кнопку")
    def click_logout_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "#nav-logout").click()

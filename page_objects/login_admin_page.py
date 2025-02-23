import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginAdminPage(BasePage):
    PATH = "/administration"

    @allure.step("Проверяю, что заголовок отображается")
    def title_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '[title="OpenCart"]')
        return True

    @allure.step("Проверяю, что заголовок над полем ввода имени пользователя отображается")
    def username_title_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.mb-3 [for="input-username"]')
        return True

    @allure.step("Проверяю, что поле для ввода имени пользователя отображается")
    def username_field_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#input-username")
        return True

    @allure.step("Проверяю, что заголовок над полем ввода пароля отображается")
    def password_title_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.mb-3 [for="input-password"]')
        return True

    @allure.step("Проверяю, что поле для ввода пароля отображается")
    def password_field_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#input-password")
        return True

    @allure.step("Проверяю, что кнопка login отображается")
    def login_button_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#form-login > div.text-end > button")
        return True

    @allure.step("Ввожу креды админа")
    def login_with_admin_creads(self, login: str, password: str):
        self.driver.find_element(By.CSS_SELECTOR, "#input-username").send_keys(login)
        self.driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "#form-login > div.text-end > button"
        ).click()

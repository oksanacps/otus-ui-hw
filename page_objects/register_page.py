import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    PATH = "/en-gb?route=account/register"

    @allure.step("Проверяю, что заголовок отображается")
    def header_is_visible(self):
        return self.is_visible((By.CSS_SELECTOR, "#content > h1"))

    @allure.step("Проверяю, что поле для ввода имени отображается")
    def first_name_input_is_visible(self):
        return self.is_visible((By.ID, "input-firstname"))

    @allure.step("Проверяю, что поле для ввода фамилии отображается")
    def last_name_input_is_visible(self):
        return self.is_visible((By.ID, "input-lastname"))

    @allure.step("Проверяю, что поле для ввода почты отображается")
    def email_input_is_visible(self):
        return self.is_visible((By.ID, "input-email"))

    @allure.step("Проверяю, что поле для ввода пароля отображается")
    def password_input_is_visible(self):
        return self.is_visible((By.ID, "input-password"))

    @allure.step("Проверяю, что тогл согласия с политикой отображается")
    def policy_checkbox_is_visible(self):
        return self.is_visible((By.CSS_SELECTOR, "#form-register > div > div > input"))

    @allure.step("Проверяю, что кнопка подтверждения регистрации отображается")
    def submit_button_is_visible(self):
        return self.is_visible((By.CSS_SELECTOR, "#form-register > div > button"))

    @allure.step("Заполняю обязательны поля при регистрации")
    def input_client_data_to_required_field(
        self, first_name, last_name, email, password
    ):
        self.send_keys(first_name, (By.ID, "input-firstname"))
        self.send_keys(last_name, (By.ID, "input-lastname"))
        self.send_keys(email, (By.ID, "input-email"))
        self.send_keys(password, (By.ID, "input-password"))

    @allure.step("Включаю тогл согласия с политикой")
    def check_policy_checkbox(self):
        self.click((By.CSS_SELECTOR, "#form-register > div > div > input"))

    @allure.step("Нажимаю на кнопку подтверждения регистрации")
    def click_submit_button(self):
        self.click((By.CSS_SELECTOR, "#form-register > div > button"))

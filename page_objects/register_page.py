import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    PATH = "/en-gb?route=account/register"

    @allure.step("Проверяю, что заголовок отображается")
    def header_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#content > h1")
        return True

    @allure.step("Проверяю, что поле для ввода имени отображается")
    def first_name_input_is_visible(self):
        self.driver.find_element(By.ID, "input-firstname")
        return True

    @allure.step("Проверяю, что поле для ввода фамилии отображается")
    def last_name_input_is_visible(self):
        self.driver.find_element(By.ID, "input-lastname")
        return True

    @allure.step("Проверяю, что поле для ввода почты отображается")
    def email_input_is_visible(self):
        self.driver.find_element(By.ID, "input-email")
        return True

    @allure.step("Проверяю, что поле для ввода пароля отображается")
    def password_input_is_visible(self):
        self.driver.find_element(By.ID, "input-password")
        return True

    @allure.step("Проверяю, что тогл согласия с политикой отображается")
    def policy_checkbox_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#form-register > div > div > input")
        return True

    @allure.step("Проверяю, что кнопка подтверждения регистрации отображается")
    def submit_button_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#form-register > div > button")
        return True

    @allure.step("Заполняю обязательны поля при регистрации")
    def input_client_data_to_required_field(
        self, first_name, last_name, email, password
    ):
        self.driver.find_element(By.ID, "input-firstname").send_keys(first_name)
        self.driver.find_element(By.ID, "input-lastname").send_keys(last_name)
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)

    @allure.step("Включаю тогл согласия с политикой")
    def check_policy_checkbox(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#form-register > div > div > input"
        ).click()

    @allure.step("Нажимаю на кнопку подтверждения регистрации")
    def click_submit_button(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#form-register > div > button"
        ).click()

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginAdminPage(BasePage):
    PATH = "/administration"

    def title_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '[title="OpenCart"]')
        return True

    def username_title_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.mb-3 [for="input-username"]')
        return True

    def username_field_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#input-username")
        return True

    def password_title_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.mb-3 [for="input-password"]')
        return True

    def password_field_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#input-password")
        return True

    def login_button_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#form-login > div.text-end > button")
        return True

    def login_with_admin_creads(self, login: str, password: str):
        self.driver.find_element(By.CSS_SELECTOR, "#input-username").send_keys(login)
        self.driver.find_element(By.CSS_SELECTOR, "#input-password").send_keys(password)
        self.driver.find_element(
            By.CSS_SELECTOR, "#form-login > div.text-end > button"
        ).click()

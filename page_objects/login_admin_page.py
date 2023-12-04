from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginAdminPage(BasePage):
    PATH = '/admin'

    def title_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.panel-title')
        return True

    def username_title_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.form-group > [for="input-username"]')
        return True

    def username_field_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.input-group > [type="text"]')
        return True

    def password_title_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.form-group > [for="input-password"]')
        return True

    def password_field_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.input-group > [type="password"]')
        return True

    def forgotten_password_button_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '[.help-block > a]')
        return True

    def login_button_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.text-right > [type="submit"]')
        return True

    def login_with_admin_creads(self, login: str, password: str):
        self.driver.find_element(By.CSS_SELECTOR, '.input-group > [type="text"]').send_keys(login)
        self.driver.find_element(By.CSS_SELECTOR, '.input-group > [type="password"]').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '.text-right > [type="submit"]').click()

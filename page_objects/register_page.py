from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    PATH = "/en-gb?route=account/register"

    def header_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#content > h1")
        return True

    def first_name_input_is_visible(self):
        self.driver.find_element(By.ID, "input-firstname")
        return True

    def last_name_input_is_visible(self):
        self.driver.find_element(By.ID, "input-lastname")
        return True

    def email_input_is_visible(self):
        self.driver.find_element(By.ID, "input-email")
        return True

    # def telephone_input_is_visible(self):
    #     self.driver.find_element(By.ID, 'input-telephone')
    #     return True

    def password_input_is_visible(self):
        self.driver.find_element(By.ID, "input-password")
        return True

    # def confirm_input_is_visible(self):
    #     self.driver.find_element(By.ID, 'input-confirm')
    #     return True

    def policy_checkbox_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#form-register > div > div > input")
        return True

    def submit_button_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#form-register > div > button")
        return True

    def input_client_data_to_required_field(
        self, first_name, last_name, email, password
    ):
        self.driver.find_element(By.ID, "input-firstname").send_keys(first_name)
        self.driver.find_element(By.ID, "input-lastname").send_keys(last_name)
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)

    def check_policy_checkbox(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#form-register > div > div > input"
        ).click()

    def click_submit_button(self):
        self.driver.find_element(
            By.CSS_SELECTOR, "#form-register > div > button"
        ).click()

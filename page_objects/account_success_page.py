from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AccountSuccessPage(BasePage):
    PATH = ""

    def success_header_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, "#content > h1")
        return True

    def get_header_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, "#content > h1").text

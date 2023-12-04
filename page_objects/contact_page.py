from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactPage(BasePage):
    PATH = '/index.php?route=information/contact'

    def contact_form_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, 'fieldset')
        return True

    def lable_contact_form_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, 'legend')
        return True

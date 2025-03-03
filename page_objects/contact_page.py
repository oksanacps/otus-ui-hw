import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class ContactPage(BasePage):
    PATH = "/en-gb?route=information/contact"

    @allure.step("Проверяю, что форма с еонтактными данными отображается")
    def contact_form_is_visible(self):
        return self.is_visible((By.CSS_SELECTOR, "fieldset"))

    @allure.step("Проверяю, что заголовок в форме с контактами, отображается")
    def lable_contact_form_is_visible(self):
        return self.is_visible((By.CSS_SELECTOR, "legend"))

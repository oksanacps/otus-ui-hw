from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    PATH = ""

    def open_products_list(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="parent collapsed"]').click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#menu-catalog > .collapse > .active"
        ).click()

    def open_add_product_form(self):
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Add New"]').click()

    def fill_required_fields_for_new_product(self, product_name, meta_tag, model, seo):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="product_description[1][name]"]'
        ).send_keys(product_name)
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="product_description[1][meta_title]"]'
        ).send_keys(meta_tag)
        self.driver.find_element(By.CSS_SELECTOR, '[class="nav-link active"]').click()
        self.driver.find_element(By.ID, "input-model").send_keys(model)
        self.driver.find_element(By.CSS_SELECTOR, '[href="#tab-seo"]').click()
        self.driver.find_element(By.ID, "#input-keyword-0-1l").send_keys(seo)

    def click_save_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Save"]').click()

    def number_of_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "tbody > tr")

    def get_attributes_new_product(self, number):
        product_name = self.driver.find_element(
            By.CSS_SELECTOR,
            "tbody > tr:nth-child(" + str(number) + ") > td:nth-child(3)",
        ).text
        model = self.driver.find_element(
            By.CSS_SELECTOR,
            "tbody > tr:nth-child(" + str(number) + ") > td:nth-child(4)",
        ).text

        return product_name, model

    def select_product_in_list(self):
        self.driver.find_element(By.NAME, "selected[]").click()

    def delete_product(self):
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Delete"]').click()

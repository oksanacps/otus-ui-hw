from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    PATH = ''

    def open_products_list(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="parent"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.collapse > .active').click()

    def open_add_product_form(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-original-title="Add New"]').click()

    def fill_required_fields_for_new_product(self, product_name, meta_tag, model):
        self.driver.find_element(By.ID, 'input-name1').send_keys(product_name)
        self.driver.find_element(By.ID, 'input-meta-title1').send_keys(meta_tag)
        self.driver.find_element(By.CSS_SELECTOR, '#form-product > ul > li.active > a').click()
        self.driver.find_element(By.ID, 'input-model').send_keys(model)

    def click_save_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="fa fa-save"]').click()

    def number_of_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR, 'tbody > tr')

    def get_attributes_new_product(self, number):
        product_name = self.driver.find_element(By.CSS_SELECTOR,
                                                'tbody > tr:nth-child(' + str(number) + ') > td:nth-child(3)').text
        model = self.driver.find_element(By.CSS_SELECTOR,
                                         'tbody > tr:nth-child(' + str(number) + ') > td:nth-child(4)').text

        return product_name, model

import allure

from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminPage(BasePage):
    PATH = ""

    @allure.step("Открываю страницу с товарами")
    def open_products_list(self):
        self.click((By.CSS_SELECTOR, '[class="parent collapsed"]', "parent collapsed"))

    @allure.step("Открываю форму добавления товара в базу")
    def open_add_product_form(self):
        self.click((By.CSS_SELECTOR, '[aria-label="Add New"]', "add_product_form"))
        self.click((By.CSS_SELECTOR, "#menu-catalog > .collapse > .active"))

    @allure.step("Заполняю обязательные поля в карте добавления товара")
    def fill_required_fields_for_new_product(self, product_name, meta_tag, model, seo):
        self.send_keys(
            (
                product_name,
                By.CSS_SELECTOR,
                '[name="product_description[1][name]"]',
                "product_description_name",
            )
        )
        self.send_keys(
            (
                meta_tag,
                By.CSS_SELECTOR,
                '[name="product_description[1][meta_title]"]',
                "product_description_meta_title",
            )
        )
        self.click((By.CSS_SELECTOR, '[class="nav-link active"]', "nav-link active"))
        self.send_keys(model, (By.ID, "input-model", "input-model"))
        self.click((By.CSS_SELECTOR, '[href="#tab-seo"]', "tab-seo"))
        self.send_keys(seo, (By.ID, "#input-keyword-0-1l", "input-keyword"))

    @allure.step("Нажимаю на кнопку сохранения")
    def click_save_button(self):
        self.click((By.CSS_SELECTOR, '[aria-label="Save"]', 'label="Save"'))

    @allure.step("Проверяю кол-во товаров")
    def number_of_product(self):
        return self.find_element_with_screenshot(By.CSS_SELECTOR, "tbody > tr", "table")

    @allure.step("Получаю свойства добавленного товара")
    def get_attributes_new_product(self, number):
        product_name = self.get_text(
            By.CSS_SELECTOR,
            "tbody > tr:nth-child(" + str(number) + ") > td:nth-child(3)",
            "character_1",
        )
        model = self.get_text(
            By.CSS_SELECTOR,
            "tbody > tr:nth-child(" + str(number) + ") > td:nth-child(4)",
            "character_2",
        )

        return product_name, model

    @allure.step("Выбираю товар в списке")
    def select_product_in_list(self):
        self.click((By.NAME, "selected[]", "checkbox"))

    @allure.step("Удаляю товар")
    def delete_product(self):
        self.click((By.CSS_SELECTOR, '[aria-label="Delete"]', "delete_button"))

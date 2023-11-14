from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminHomePage(BasePage):
    PATH = ''

    def user_profile_is_visible(self):
        self.driver.find_element(By.CSS_SELECTOR, '.dropdown-toggle > [alt="John Doe"]')
        return True

    def click_logout_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[class="nav navbar-nav navbar-right"] > li:nth-child(2)').click()

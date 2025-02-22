from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    PATH = "/en-gb?route=account/login"

    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
    MY_ACCOUNT_HEADER = (By.CSS_SELECTOR, "#content > h2:nth-child(1)")

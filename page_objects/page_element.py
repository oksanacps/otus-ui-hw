from selenium.webdriver.common.by import By


class Header:
    CARET = (By.CSS_SELECTOR, "#form-currency > div > a > i")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[href$="logout"]')

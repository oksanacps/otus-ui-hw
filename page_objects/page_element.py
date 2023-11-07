from selenium.webdriver.common.by import By

class Header():
    CARET = (By.CSS_SELECTOR, '.caret')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.list-inline > .dropdown > .dropdown-menu > li:nth-child(5)')
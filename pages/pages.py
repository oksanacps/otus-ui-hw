from selenium.webdriver.common.by import By


class HomePage:
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search')
    CATEGORIES = (By.CSS_SELECTOR, "[class='nav navbar-nav'] > li")


class MacPage:
    SHOPPING_CART_MAC = (By.CSS_SELECTOR, '.button-group > button:nth-child(1)')


class ContactPage:
    CONTACT_FORM = (By.CSS_SELECTOR, 'fieldset')
    LABLE_CONTACT_FORM = (By.CSS_SELECTOR, 'legend')


class SearchPage:
    BUTTON_SEARCH = (By.ID, 'button-search')


class LoginPage:
    EMAIL = (By.ID, 'input-email')
    PASSWORD = (By.ID, 'input-password')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    MY_ACCOUNT_HEADER = (By.CSS_SELECTOR, '.col-sm-9 > h2:nth-child(1)')


class Header:
    CARET = (By.CSS_SELECTOR, '.caret')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.list-inline > .dropdown > .dropdown-menu > li:nth-child(5)')


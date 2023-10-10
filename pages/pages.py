from selenium.webdriver.common.by import By


class HomePage:
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search')
    CATEGORIES = (By.CSS_SELECTOR, "[class='nav navbar-nav'] > li")
    LOGO = (By.ID, 'logo')
    CART = (By.ID, 'cart')
    PRODUCTS = (By.CSS_SELECTOR, '.row > div > [class="product-thumb transition"]')
    CART_BUTTON = (By.CSS_SELECTOR, '.button-group > [type="button"] > [class="fa fa-shopping-cart"]')
    PRODUCTS_IN_CART = (By.CSS_SELECTOR, '[class="table table-striped"] > tbody > tr')
    CURRENCY_DROP_DOWN = (By.CSS_SELECTOR, '[class="fa fa-caret-down"]')
    EURO = (By.CSS_SELECTOR, '[name="EUR"]')
    POUND = (By.CSS_SELECTOR, '[name="GBP"]')
    USD = (By.CSS_SELECTOR, '[name="USD"]')
    PRICE = (By.CSS_SELECTOR, '.price-new')


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


class LoginAdminPage:
    TITLE = (By.CSS_SELECTOR, '.panel-title')
    USERNAME_TITLE = (By.CSS_SELECTOR, '.form-group > [for="input-username"]')
    USERNAME_FIELD = (By.CSS_SELECTOR, '.input-group > [type="text"]')
    PASSWORD_TITLE = (By.CSS_SELECTOR, '.form-group > [for="input-password"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '.input-group > [type="password"]')
    FORGOTTEN_PASSWORD_BUTTON = (By.CSS_SELECTOR, '[.help-block > a]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.text-right > [type="submit"]')


class AdminHomePage:
    USER_PROFILE = (By.CSS_SELECTOR, '.dropdown-toggle > [alt="John Doe"]')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '[class="nav navbar-nav navbar-right"] > li:nth-child(2)')


class RegisterPage:
    HEADER = (By.CSS_SELECTOR, '.col-sm-9 > h1')
    FIRST_NAME_INPUT = (By.ID, 'input-firstname')
    LAST_NAME_INPUT = (By.ID, 'input-lastname')
    EMAIL_INPUT = (By.ID, 'input-email')
    TELEPHONE_INPUT = (By.ID, 'input-telephone')
    PASSWORD_INPUT = (By.ID, 'input-password')
    CONFIRM_INPUT = (By.ID, 'input-confirm')
    POLICY_CHECKBOX = (By.CSS_SELECTOR, '.pull-right > [name="agree"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '.pull-right > [type="submit"]')


class ProductCardPage:
    IMAGES = (By.CSS_SELECTOR, '.thumbnails > li')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-4 > h1')
    PRICE = (By.CSS_SELECTOR, '.col-sm-4 > .list-unstyled > li > h2')
    ADD_CART_BUTTON = (By.ID, 'button-cart')
    DESCRIPTION = (By.ID, 'tab-description')


class CatalogPage:
    BREADCRUMBS = (By.CSS_SELECTOR, '.breadcrumb')
    CATALOG_HEADER = (By.CSS_SELECTOR, '.col-sm-9 > h2')
    PRODUCTS = (By.CSS_SELECTOR, '.row > div > .product-thumb')
    CART_BUTTON = (By.CSS_SELECTOR, '.button-group > [type="button"] > [class="fa fa-shopping-cart"]')
    PRODUCT_HEADER = (By.CSS_SELECTOR, '.caption > h4')
    PRICE = (By.CSS_SELECTOR, '.price')

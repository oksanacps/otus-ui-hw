import random
import string
import pytest
import allure

from selenium import webdriver as webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from page_objects.home_page import HomePage


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Options: firefox, chrome, opera. Default: chrome",
        choices=("chrome", "firefox", "opera"),
    )
    parser.addoption("--base_url", help="base_url")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture()
def driver(request):
    global browser
    browser_name = request.config.getoption("--browser")
    service = ChromeService()

    if browser_name == "chrome":
        browser = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        browser = webdriver.Firefox(service=service)
    elif browser_name == "opera":
        browser = webdriver.Chrome(service=service)

    yield browser

    browser.close()


@pytest.fixture()
def clear_cart(driver, base_url):
    with allure.step("SetUp. Очищаю корзину перед тестом"):
        home_page = HomePage(driver)
        home_page.open(base_url)

        home_page.click_cart()
        product_number = home_page.number_of_products_in_cart()
        if product_number > 0:
            for product in range(product_number):
                driver.find_element(
                    By.XPATH,
                    '//*[@id="header-cart"]/div/ul/li/table/tbody/tr/td[5]/form/button',
                )

    yield

    with allure.step("TearDown. Очищаю корзину после теста"):
        product_number = home_page.number_of_products_in_cart()
        if product_number > 0:
            for product in range(product_number):
                driver.find_element(
                    By.XPATH,
                    '//*[@id="header-cart"]/div/ul/li/table/tbody/tr/td[5]/form/button',
                )


@allure.step("Генерирую email")
@pytest.fixture()
def random_email():
    random_email = ""
    for x in range(10):
        random_email += "".join(random.choice(string.ascii_lowercase))
    yield random_email + "@gmail.com"

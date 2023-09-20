from selenium import webdriver as webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from pages.pages import HomePage

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Options: firefox, chrome, opera. Default: chrome",
        choices=("chrome", "firefox", "opera")
    )
    parser.addoption(
        "--base_url",
        help="base_url"
    )


@pytest.fixture()
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
    browser = driver
    browser.get(base_url)

    browser.find_element(*HomePage.CART).click()
    product_number = len(browser.find_elements(*HomePage.PRODUCTS_IN_CART))
    if product_number > 0:
        for product in range(product_number):
            browser.find_element(By.CSS_SELECTOR, '[title="Remove"]')

    yield

    browser.find_element(*HomePage.CART).click()
    product_number = len(browser.find_elements(*HomePage.PRODUCTS_IN_CART))
    if product_number > 0:
        for product in range(product_number):
            browser.find_element(By.CSS_SELECTOR, '[title="Remove"]')

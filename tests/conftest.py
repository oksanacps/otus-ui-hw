import pytest
import os

from selenium import webdriver as webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from pages.pages import Header


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
def logout(driver, base_url):
    browser = driver
    browser.get(base_url)
    browser.find_element(*Header.CARET).click()
    logout_button = browser.find_elements(*Header.LOGOUT_BUTTON)
    if len(logout_button) > 0:
        logout_button.click()

    yield

    browser.find_element(*Header.CARET).click()
    browser.find_element(*Header.LOGOUT_BUTTON).click()


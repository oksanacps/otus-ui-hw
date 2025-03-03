import logging
import os
import allure

import selenium
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.__config_logger()

    def __config_logger(self, to_file=False):
        self.logger = logging.getLogger(type(self).__name__)
        os.makedirs("logs", exist_ok=True)
        if to_file:
            self.logger.addHandler(
                logging.FileHandler(f"logs/{self.driver.test_name}.log")
            )
        self.logger.setLevel(level=logging.DEBUG)

    def open(self, base_url, path=""):
        self.logger.info(f"Open {base_url + path}")
        self.driver.get(base_url + path)

    def click(self, locator):
        self.logger.info(f"Click {locator}")
        element = self.find_element_with_screenshot(*locator)
        element.click()

    def send_keys(self, keys, locator):
        self.logger.info(f"Send keys to {locator}")
        element = self.find_element_with_screenshot(*locator)
        element.send_keys(keys)

    def get_text(self, locator):
        self.logger.info(f"Send keys to {locator}")
        element = self.find_element_with_screenshot(*locator)
        return element.text()

    def is_visible(self, locator):
        try:
            self.logger.info(f"Check that {locator} is visible")
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)
            )
        except selenium.common.exceptions.TimeoutException:
            raise AssertionError

    def is_presence(self, locator):
        try:
            self.logger.info(f"Check that {locator} is present")
            return WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(locator)
            )
        except selenium.common.exceptions.TimeoutException:
            raise AssertionError

    def find_element_with_screenshot(
        self, by, value, screenshot_name="screenshot_image"
    ):
        try:
            return self.driver.find_element(by, value)
        except NoSuchElementException as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=screenshot_name,
                attachment_type=allure.attachment_type.PNG,
            )
            raise AssertionError(e.msg)

    def find_elements_with_screenshot(
        self, by, value, screenshot_name="screenshot_image"
    ):
        try:
            return self.driver.find_elements(by, value)
        except NoSuchElementException as e:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name=screenshot_name,
                attachment_type=allure.attachment_type.PNG,
            )
            raise AssertionError(e.msg)

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, base_url, path=''):
        self.driver.get(base_url + path)

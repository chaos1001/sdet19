import time

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver_base: webdriver = None):
        self.driver = driver_base
        if not self.driver:
            driver_path = "/Users/ch/dev/lib/chromedriver"
            self.driver = webdriver.Chrome(executable_path=driver_path)
            self.driver.implicitly_wait(3)

    def find(self, by, locator) -> WebElement:
        element = self.driver.find_element(by, locator)
        return element

    def finds(self, by, locator):
        elements = self.driver.find_elements(by, locator)
        return elements

    def find_and_click(self, by, locator):
        element = self.driver.find_element(by, locator)
        element.click()

    def wait_for_click(self, by, locator, timeout=10):
        element: WebElement = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((by, locator)))
        element.click()

    def close_driver(self):
        self.driver.close()

    def take_screenshot(self):
        screenshot_file = "./logs/screenshot-{}.png".format(int(time.time()))
        self.driver.save_screenshot(screenshot_file)
        return screenshot_file

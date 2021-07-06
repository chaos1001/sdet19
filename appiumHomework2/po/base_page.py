import time
import logging
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

IMPLICITLY_WAIT_DEFAULT = 10


class Page(object):
    def __init__(self, driver: webdriver = None):
        self.driver = driver

    def find(self, by, locator) -> WebElement:
        element = self.driver.find_element(by, locator)
        return element

    def finds(self, by, locator):
        logging.info("finding locator: {}".format(locator))
        elements = self.driver.find_elements(by, locator)
        return elements

    def find_and_click(self, by, locator):
        logging.info("find and click locator: {}".format(locator))
        element = self.driver.find_element(by, locator)
        element.click()

    def find_and_sendkeys(self, by, locator, text):
        logging.info("find and send_keys locator: {}".format(locator))
        element = self.driver.find_element(by, locator)
        element.send_keys(text)

    def wait_for_click(self, by, locator, timeout=10):
        logging.info("wait for click locator: {}".format(locator))
        element: WebElement = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable((by, locator)))
        element.click()

    def close_driver(self):
        self.driver.close()

    def take_screenshot(self):
        screenshot_file = "./logs/screenshot-{}.png".format(int(time.time()))
        self.driver.save_screenshot(screenshot_file)
        return screenshot_file

    def swipe_find(self, by, locator, retry_times=5):
        self.driver.implicitly_wait(1)
        for i in range(retry_times):
            while True:
                try:
                    element = self.driver.find_element(by, locator)
                    self.driver.implicitly_wait(IMPLICITLY_WAIT_DEFAULT)
                    return element
                except:
                    logging.info("未找到元素：{}，继续滑动".format(locator))
                    size = self.driver.get_window_size()
                    width = size['width']
                    height = size['height']

                    start_x = width/2
                    start_y = height*4/5
                    end_x = width/2
                    end_y = height*1/5
                    duration = 2000
                    self.driver.swipe(start_x, start_y, end_x, end_y, duration)

                if i == retry_times - 1:
                    self.driver.implicitly_wait(IMPLICITLY_WAIT_DEFAULT)
                    raise NoSuchElementException("找了 {} 次，没找到".format(i))

    def get_toast_text(self):
        text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").get_attribute('text')
        return text

    def back(self, times=1):
        for i in range(times):
            self.driver.back()

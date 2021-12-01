import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHog:
    def setup(self):
        driver_path = "/Users/ch/dev/lib/chromedriver"
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get('https://home.testing-studio.com')
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_hog(self):
        category_name = (By.CSS_SELECTOR, "#ember195 .category-name")
        self.driver.find_element_by_link_text("所有分类").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(category_name))
        self.driver.find_element(*category_name).click()

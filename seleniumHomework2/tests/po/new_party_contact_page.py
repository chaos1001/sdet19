import time
from selenium.webdriver.common.by import By
from seleniumHomework2.tests.po.base_page import BasePage


class NewPartyContactPage(BasePage):
    _PARTY_NAME = (By.ID, 'party_name')

    def get_party_name(self):
        # 等待动画结束
        time.sleep(2)
        return self.find(*self._PARTY_NAME).text

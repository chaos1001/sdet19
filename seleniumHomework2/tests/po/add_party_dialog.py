from selenium.webdriver.common.by import By

from seleniumHomework2.tests.po.base_page import BasePage
from seleniumHomework2.tests.po.new_party_contact_page import NewPartyContactPage


class AddPartyDialog(BasePage):
    _PARTY_NAME = (By.NAME, "name")
    _PARTY_LIST = (By.CLASS_NAME, "js_toggle_party_list")
    _PARTY_ROOT = (By.ID, "1688849969965621_anchor")
    _PARENT_PARTY_TEXT = (By.LINK_TEXT, "{}")
    _CONFIRM = (By.LINK_TEXT, "确定")
    _TIPS = (By.ID, "js_tips")

    def add_party_with_name(self, name, parent_party_name=None):
        self.find(*self._PARTY_NAME).send_keys(name)
        self.find_and_click(*self._PARTY_LIST)
        if not parent_party_name:
            self.finds(*self._PARTY_ROOT)[1].click()
        else:
            self.finds(By.LINK_TEXT, parent_party_name)[1].click()
        self.find(*self._CONFIRM).click()
        return NewPartyContactPage(self.driver)

    def add_party_with_name_fail(self, name):
        self.find(*self._PARTY_NAME).send_keys(name)
        self.find_and_click(*self._PARTY_LIST)
        self.find(*self._CONFIRM).click()
        return self

    def get_tips_text(self):
        return self.find(*self._TIPS).text

from selenium.webdriver.common.by import By
from seleniumHomework2.tests.po.add_party_dialog import AddPartyDialog
from seleniumHomework2.tests.po.base_page import BasePage


class ContactPage(BasePage):
    _ADD_MEMBER = (By.XPATH, '//*[@id="main"]/div/div/div[2]/div/div[2]/div[3]/div[1]/a[1]')
    _MEMBER_LIST = (By.XPATH, '//*[@id="member_list"]/tr')
    _PLUS_ICON = (By.CLASS_NAME, 'member_colLeft_top_addBtn')
    _CREATE_PARTY = (By.CLASS_NAME, 'js_create_party')

    def click_add_member(self):
        self.wait_for_click(*self._ADD_MEMBER)

        from seleniumHomework2.tests.po.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)

    def click_add_party(self):
        self.find_and_click(*self._PLUS_ICON)
        self.find_and_click(*self._CREATE_PARTY)
        return AddPartyDialog(self.driver)

    def get_members_name(self):
        total_member = self.finds(*self._MEMBER_LIST)
        members_name = []
        for i in range(1, len(total_member) + 1):
            members_name.append(self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[{}]/td[2]/span'.format(i)).text)
        return members_name

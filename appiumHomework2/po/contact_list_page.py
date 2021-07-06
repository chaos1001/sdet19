from appium.webdriver.common.mobileby import MobileBy
from appiumHomework2.po.base_page import Page


class ContactListPage(Page):
    _ADD_CONTACT = (MobileBy.XPATH, "//*[@text='添加成员']")
    _MANAGE_CONTACT = (MobileBy.ID, "com.tencent.wework:id/gup")
    _QUIT_MANAGE_CONTACT = (MobileBy.ID, "com.tencent.wework:id/guk")

    def goto_add_contact_page(self):
        from appiumHomework2.po.add_contact_page import AddContactPage
        # 点击添加成员
        self.swipe_find(*self._ADD_CONTACT, 10).click()
        # self.driver.find_element(*self._ADD_CONTACT).click()
        return AddContactPage(self.driver)

    def manage_contact_page(self):
        self.find_and_click(*self._MANAGE_CONTACT)
        return self

    def goto_edit_contact_page(self, contact_name):
        self.swipe_find(MobileBy.XPATH, "//*[@text='{}']".format(contact_name)).click()
        from appiumHomework2.po.edit_contact_page import EditContactPage
        return EditContactPage(self.driver)

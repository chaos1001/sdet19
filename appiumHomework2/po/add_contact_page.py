from appium.webdriver.common.mobileby import MobileBy
from appiumHomework2.po.base_page import Page


class AddContactPage(Page):
    _ADD_CONTACT_MANUAL = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _ADD_FAIL_RESULT = (MobileBy.ID, "com.tencent.wework:id/b_1")

    def add_contact_manual(self):
        from appiumHomework2.po.edit_contact_page import EditContactPage
        self.find_and_click(*self._ADD_CONTACT_MANUAL)
        return EditContactPage(self.driver)

    def get_add_success_result(self):
        toast_text = self.get_toast_text()
        return toast_text

    def get_add_fail_result(self):
        return self.find(*self._ADD_FAIL_RESULT).text

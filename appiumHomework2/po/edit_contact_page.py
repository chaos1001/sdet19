from appium.webdriver.common.mobileby import MobileBy

from appiumHomework2.po.base_page import Page


class EditContactPage(Page):
    _NAME_EDIT_TEXT = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText")
    _PHONE_NUMBER_EDIT_TEXT = (MobileBy.XPATH, "//*[contains(@text, '手机')]/..//android.widget.EditText")
    _EMAIL_EDIT_TEXT = (MobileBy.XPATH, "//*[contains(@text, '邮箱')]/../android.widget.EditText")
    _SET_PARTY_BUTTON = (MobileBy.XPATH, "//*[@text='设置部门']")
    _SET_PARTY_CONFIRM_BUTTON = (MobileBy.XPATH, "//*[contains(@text,'确定')]")
    _INVITE_CHECKBOX = (MobileBy.XPATH, "//*[@text='保存后自动发送邀请通知']")
    _SAVE = (MobileBy.XPATH, "//*[@text='保存']")
    _DELETE = (MobileBy.XPATH, "//*[contains(@text,'删除成员')]")
    _DELETE_CONFIRM = (MobileBy.XPATH, "//*[contains(@text,'确定')]")
    _CANCEL_EDIT = (MobileBy.XPATH, "//*[contains(@text,'取消')]")

    def edit_contact(self, fake_name, fake_phone_number, fake_email):
        from appiumHomework2.po.add_contact_page import AddContactPage
        # 姓名
        self.find_and_sendkeys(*self._NAME_EDIT_TEXT, fake_name)
        # 手机
        self.find_and_sendkeys(*self._PHONE_NUMBER_EDIT_TEXT, fake_phone_number)
        self.find_and_sendkeys(*self._EMAIL_EDIT_TEXT, fake_email)
        self.find_and_click(*self._SET_PARTY_BUTTON)
        self.find_and_click(*self._SET_PARTY_CONFIRM_BUTTON)
        self.find_and_click(*self._INVITE_CHECKBOX)
        self.find_and_click(*self._SAVE)
        return AddContactPage(self.driver)

    def delete_contact(self):
        self.find_and_click(*self._DELETE)
        self.find_and_click(*self._DELETE_CONFIRM)
        from appiumHomework2.po.contact_list_page import ContactListPage
        return ContactListPage(self.driver)

    def quit_edit_contact(self):
        self.back()
        self.back()
        self.find_and_click(*self._CANCEL_EDIT)
        from appiumHomework2.po.add_contact_page import AddContactPage
        return AddContactPage(self.driver)

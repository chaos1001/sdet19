from appium.webdriver.common.mobileby import MobileBy
from appiumHomework2.po.base_page import Page


class MainPage(Page):
    _CONTACT_MENU = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contact_list(self):
        from appiumHomework2.po.contact_list_page import ContactListPage
        # 点通讯录  text:通讯录 resource-id:com.tencent.wework:id/dqn
        self.find_and_click(*self._CONTACT_MENU)
        return ContactListPage(self.driver)

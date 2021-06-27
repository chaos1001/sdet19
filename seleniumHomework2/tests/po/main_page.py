from selenium.webdriver.common.by import By

from seleniumHomework2.tests.po.base_page import BasePage


class MainPage(BasePage):
    _CONTACT = (By.ID, "menu_contacts")

    def goto_contact_page(self):
        self.find_and_click(*self._CONTACT)
        from seleniumHomework2.tests.po.contact_page import ContactPage
        return ContactPage(self.driver)


import time
from selenium.webdriver.common.by import By
from seleniumHomework2.tests.po.base_page import BasePage


class AddMemberPage(BasePage):
    _USERNAME_INPUT = (By.ID, 'username')
    _ACCTID_INPUT = (By.ID, 'memberAdd_acctid')
    _PHONE_INPUT = (By.ID, 'memberAdd_phone')
    _TELEPHONE_INPUT = (By.ID, 'memberAdd_telephone')
    _EMAIL_INPUT = (By.ID, 'memberAdd_mail')
    _ADDRESS_INPUT = (By.ID, 'memberEdit_address')
    _TITLE_INPUT = (By.ID, 'memberAdd_title')
    _INVITE_CHECKBOX = (By.NAME, 'sendInvite')
    _SAVE_BUTTON = (By.XPATH, '//*[@id="main"]/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]')

    def edit_member(self):
        postfix = int(time.time())
        username = "员工-{}".format(postfix)
        self.find(*self._USERNAME_INPUT).send_keys(username)
        self.find(*self._ACCTID_INPUT).send_keys("yuangong-{}".format(postfix))
        self.find(*self._PHONE_INPUT).send_keys("131{}".format(str(postfix)[2:]))
        self.find(*self._TELEPHONE_INPUT).send_keys("876543")
        self.find(*self._EMAIL_INPUT).send_keys("yuangong-{}@moxianb.com".format(postfix))
        self.find(*self._ADDRESS_INPUT).send_keys("moxiandadao1001")
        self.find(*self._TITLE_INPUT).send_keys("普通员工")
        self.find(*self._INVITE_CHECKBOX).click()
        self.find(*self._SAVE_BUTTON).click()

        from seleniumHomework2.tests.po.contact_page import ContactPage
        return ContactPage(self.driver)

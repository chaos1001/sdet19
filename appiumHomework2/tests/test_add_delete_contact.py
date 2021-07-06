import time
import allure
import logging
from faker import Faker

from appiumHomework2.po.app import App


class TestAddDeleteContact:
    def setup_class(self):
        self.fake = Faker("zh_CN")
        self.fake_name = self.fake.name()
        self.fake_phone_number = self.fake.phone_number()
        self.fake_email = self.fake.email()
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back(5)
        # self.app.restart()

    def teardown_class(self):
        self.app.quit()

    @allure.story("添加成员成功")
    def test_add_contact_success(self):
        # 验证弹出的toast
        toast_text = self.main.goto_contact_list().goto_add_contact_page().add_contact_manual().edit_contact(self.fake_name, self.fake_phone_number, self.fake_email).get_add_success_result()
        assert toast_text == "添加成功"

        screenshot_file = self.app.take_screenshot()
        with open(screenshot_file, "rb") as f:
            content = f.read()
            allure.attach(content, "添加成功", attachment_type=allure.attachment_type.PNG)

    @allure.story("添加成员失败")
    @allure.title("异常用例: 手机号重复")
    def test_add_contact_fail(self):
        edit_contact_page = self.main.goto_contact_list().goto_add_contact_page().add_contact_manual()
        fail_text = edit_contact_page.edit_contact(self.fake_name, self.fake_phone_number, self.fake_email).get_add_fail_result()
        # 验证失败提示
        assert fail_text == "手机已存在于通讯录，无法添加"

        screenshot_file = self.app.take_screenshot()
        with open(screenshot_file, "rb") as f:
            content = f.read()
            allure.attach(content, "添加失败", attachment_type=allure.attachment_type.PNG)

        edit_contact_page.quit_edit_contact()

    @allure.story("删除成员成功")
    def test_delete_contact_success(self):
        self.main.goto_contact_list().manage_contact_page().goto_edit_contact_page(self.fake_name).delete_contact()
        screenshot_file = self.app.take_screenshot()
        with open(screenshot_file, "rb") as f:
            content = f.read()
            allure.attach(content, "删除成功", attachment_type=allure.attachment_type.PNG)






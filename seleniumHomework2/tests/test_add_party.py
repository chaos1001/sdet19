import time

import allure
from seleniumHomework2.tests.po.login_page import LoginPage


@allure.title("添加部门")
class TestAddParty:
    def setup_method(self):
        self.main = LoginPage()

    def teardown_method(self):
        self.main.close_driver()

    @allure.story("添加部门成功")
    @allure.title("添加部门: 部门名称-{get_add_party_success_datas[0]}, 上级部门-{get_add_party_success_datas[1]}")
    def test_add_party_success(self, get_add_party_success_datas):
        # party_name = self.main.set_login_cookies()
        party_name = self.main.login_with_cookies().goto_contact_page().click_add_party().add_party_with_name(get_add_party_success_datas[0], get_add_party_success_datas[1]).get_party_name()
        assert get_add_party_success_datas[0] == party_name

    @allure.story("添加部门失败")
    @allure.title("添加部门: 部门名称-{get_add_party_fail_datas[0]}, 失败原因-{get_add_party_fail_datas[1]}")
    def test_add_party_fail(self, get_add_party_fail_datas):
        dialog = self.main.login_with_cookies().goto_contact_page().click_add_party().add_party_with_name_fail(
            get_add_party_fail_datas[0])
        fail_tips = dialog.get_tips_text()
        assert get_add_party_fail_datas[1] == fail_tips
        screenshot_file = dialog.take_screenshot()
        with open(screenshot_file, "rb") as f:
            content = f.read()
            allure.attach(content, "用例截图", attachment_type=allure.attachment_type.PNG)
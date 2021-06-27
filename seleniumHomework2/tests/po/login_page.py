import time

import yaml

from seleniumHomework2.tests.po.base_page import BasePage
from seleniumHomework2.tests.po.main_page import MainPage


class LoginPage(BasePage):
    def set_login_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        time.sleep(10)
        cookies = self.driver.get_cookies()

        with open("./data/cookies.yml", "wt") as f:
            f.write(yaml.safe_dump(cookies))

    def login_with_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        with open("./data/cookies.yml") as f:
            cookies = yaml.safe_load(f)
        for c in cookies:
            self.driver.add_cookie(c)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        return MainPage(self.driver)

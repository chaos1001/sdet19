import time

import allure
import pytest
import yaml
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWework:
    def setup_method(self):
        driver_path = "/Users/ch/dev/lib/chromedriver"
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.skip()
    def test_set_cookie(self):
        driver = webdriver.Chrome(executable_path="/Users/ch/dev/lib/chromedriver")
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        time.sleep(5)
        cookies = driver.get_cookies()

        with open("./data/cookies.yml", "wt") as f:
            f.write(yaml.safe_dump(cookies))

    @allure.story("添加成员成功")
    def test_add_member_success(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")

        with open("./data/cookies.yml") as f:
            cookies = yaml.safe_load(f)
        for c in cookies:
            self.driver.add_cookie(c)

        postfix = int(time.time())
        username = "员工-{}".format(postfix)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div/div[2]/div/div[2]/div[3]/div[9]/a[1]')))
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("yuangong-{}".format(postfix))
        self.driver.find_element_by_id("memberAdd_phone").send_keys("131{}".format(str(postfix)[2:]))
        self.driver.find_element_by_id("memberAdd_telephone").send_keys("876543")
        self.driver.find_element_by_id("memberAdd_mail").send_keys("yuangong-{}@moxianb.com".format(postfix))
        self.driver.find_element_by_id("memberEdit_address").send_keys("moxiandadao1001")
        self.driver.find_element_by_id("memberAdd_title").send_keys("普通员工")
        self.driver.find_element_by_name("sendInvite").click()
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="member_list"]/tr')))
        total_member = self.driver.find_elements_by_xpath('//*[@id="member_list"]/tr')
        found_new_member = False
        for i in range(1, len(total_member)+1):
            member_name = self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[{}]/td[2]/span'.format(i)).text
            if member_name == username:
                found_new_member = True

        assert found_new_member

    @allure.story("添加成员失败")
    @allure.title("异常用例: 姓名-{get_add_member_fail_datas[0]}, 账号-{get_add_member_fail_datas[1]}, 手机号-{get_add_member_fail_datas[2]}, 邮箱-{get_add_member_fail_datas[3]}")
    def test_add_member_fail(self, get_add_member_fail_datas):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")

        with open("./data/cookies.yml") as f:
            cookies = yaml.safe_load(f)
        for c in cookies:
            self.driver.add_cookie(c)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div/div[2]/div/div[2]/div[3]/div[9]/a[1]')))
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div/div[2]/div[3]/div[9]/a[1]').click()
        self.driver.find_element_by_id("username").send_keys(get_add_member_fail_datas[0])
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(get_add_member_fail_datas[0])
        self.driver.find_element_by_id("memberAdd_phone").send_keys(get_add_member_fail_datas[2])
        self.driver.find_element_by_id("memberAdd_mail").send_keys(get_add_member_fail_datas[3])
        self.driver.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()

        with pytest.raises(eval(get_add_member_fail_datas[4])):
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="member_list"]/tr')))

        screenshot_file = "./logs/screenshot-{}.png".format(int(time.time()))
        self.driver.save_screenshot(screenshot_file)
        with open(screenshot_file, "rb") as f:
            content = f.read()
            allure.attach(content, "测试图片", attachment_type=allure.attachment_type.PNG)


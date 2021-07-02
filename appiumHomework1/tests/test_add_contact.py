import time

import allure
from faker import Faker
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

fake = Faker("zh_CN")
fake_phone_number = fake.phone_number()


class TestAddContact:
    def setup_method(self):
        # 等待页面空闲的时间
        # 跳过 uiautomator2 server的安装
        # 跳过设备初始化
        # 启动之前不停止app
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0",
            "deviceName": "emulator-5554",
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.LaunchSplashActivity",
            "noReset": "true",
            "settings[waitForIdleTimeout]": 0,
            "skipServerInstallation": "true",
            "skipDeviceInitialization": "true",
            "dontStopAppOnReset": "true"
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()
        # pass

    @allure.story("添加成员成功")
    def test_add_contact_success(self):
        # 点通讯录  text:通讯录 resource-id:com.tencent.wework:id/dqn
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动直到出现添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).\
                                 instance(0)).scrollIntoView(new UiSelector().\
                                 text("添加成员").instance(0));')
        # 点击添加成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c7g").click()
        self.driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.EditText").send_keys(fake.name())
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/eq7").send_keys(fake_phone_number)
        self.driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.EditText").send_keys(fake.email())
        self.driver.find_element(MobileBy.XPATH, "//*[@text='设置部门']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'确定')]").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gur").click()
        # 验证弹出的toast
        toast_text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert toast_text == "添加成功"

        screenshot_file = "./logs/screenshot-{}.png".format(int(time.time()))
        self.driver.save_screenshot(screenshot_file)
        with open(screenshot_file, "rb") as f:
            content = f.read()
            allure.attach(content, "添加成功", attachment_type=allure.attachment_type.PNG)

        # 模拟器太卡，就不重启app了，手动还原初始状态
        self.driver.back()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='消息']").click()

    @allure.story("添加成员失败")
    @allure.title("异常用例: 手机号重复")
    def test_add_contact_fail(self):
        # 点通讯录  text:通讯录 resource-id:com.tencent.wework:id/dqn
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滚动直到出现添加成员
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).\
                                 instance(0)).scrollIntoView(new UiSelector().\
                                 text("添加成员").instance(0));')
        # 点击添加成员
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c7g").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.EditText").send_keys(
            fake.name())
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/eq7").send_keys(fake_phone_number)
        self.driver.find_element(MobileBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.RelativeLayout/android.widget.EditText").send_keys(
            fake.email())
        self.driver.find_element(MobileBy.XPATH, "//*[@text='设置部门']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'确定')]").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gur").click()
        # 验证失败提示
        fail_text = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b_1").text
        assert fail_text == "手机已存在于通讯录，无法添加"

        screenshot_file = "./logs/screenshot-{}.png".format(int(time.time()))
        self.driver.save_screenshot(screenshot_file)
        with open(screenshot_file, "rb") as f:
            content = f.read()
            allure.attach(content, "添加失败", attachment_type=allure.attachment_type.PNG)


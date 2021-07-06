import logging
from appium import webdriver

from appiumHomework2.po.base_page import Page, IMPLICITLY_WAIT_DEFAULT


class App(Page):
    def start(self):
        if self.driver is None:
            logging.info("初始化driver")
            # 等待页面空闲的时间
            # 跳过 uiautomator2 server的安装
            # 跳过设备初始化
            # 启动之前不停止app
            desired_caps = {
                "platformName": "Android",
                "platformVersion": "6.0",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": "true",
                # "settings[waitForIdleTimeout]": 0,
                # "skipServerInstallation": "true",
                "skipDeviceInitialization": "true",
                "dontStopAppOnReset": "true"
            }
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(IMPLICITLY_WAIT_DEFAULT)
        else:
            logging.info("复用driver")
            # 可以启动其他应用的activity
            self.driver.start_activity("com.tencent.wework", ".launch.WwMainActivity")
            # self.driver.launch_app()

        return self

    def restart(self):
        self.driver.close()
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        from appiumHomework2.po.main_page import MainPage
        return MainPage(self.driver)

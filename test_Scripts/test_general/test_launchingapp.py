import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from selenium.webdriver.common.by import By

from POM.meesho import Meesho

class test_launch():
    @allure.story("appium demo")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("launchapp")
    def test_launchingapp(self):
        with allure.step("automate"):
            desired_cap = {
                "appium:deviceName": "Redmi Note 8",
                "platformName": "Android",
                "appium:platformVersion": "10",
                "appium:app": "C:\\Users\\Surekha Gadhave\\Downloads\\meesho-14-0.apk"}

            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
            driver.implicitly_wait(5)
            ms = Meesho(driver)
            # ms.click_continue()
            # ms.click_close_window()
            driver.find_element(By.ID, "com.meesho.supply:id/close").click()
            # ms.click_allow()
            print("welcome to Home page of meesho")
            allure.attach(driver.get_screenshot_as_png(), name="testscreen", attachment_type=AttachmentType.PNG)
            driver.quit()

import time

import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from selenium.webdriver.common.by import By
from POM.General import General
from library.randomdata import gen_random_mobno


@allure.story("appium demo")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("automatedialnumber")
def test_dialnumber():
  mobno = gen_random_mobno()
  with allure.step("automate"):
    desired_cap = {
      "deviceName": "sdk_gphone64_x86_64",
      "platformName": "Android",
      "platformVersion": "13",
      "automationName": "UiAutomator2",
      "appPackage": "com.google.android.dialer",
      "appActivity": "com.google.android.dialer.extensions.GoogleDialtactsActivity"
    }
    driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
    driver.implicitly_wait(5)
    gs=General(driver)
    gs.click_keypad()
    time.sleep(3)
    print("welcome to phone dial")
    time.sleep(2)
    driver.find_element(By.ID,"com.google.android.dialer:id/digits").send_keys(mobno)
    time.sleep(3)
    gs.click_callbtn()
    time.sleep(3)
    allure.attach(driver.get_screenshot_as_png(), name="Dialscreen", attachment_type=AttachmentType.PNG)
    gs.click_endcall()
    print("Automatic dial number working perfectly")
import time
from appium import webdriver
from POM.meesho import Meesho


def test_screenshot():
    desired_cap = {
        "appium:deviceName": "sdk_gphone64_x86_64",
        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:app": "C:\\Users\\Surekha Gadhave\\Downloads\\meesho-14-0.apk"}

    # create driver instance
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    driver.implicitly_wait(5)
    ms = Meesho(driver)
    # ms.click_continue()
    # close window
    ms.click_close_window()
    # click allow
    ms.click_allow()
    time.sleep(3)
    print("welcome to Home page of meesho")
    ts=time.strftime("%Y_%m_%d_%H%M%S")
    activityname=driver.current_activity
    filename=activityname+ts
    time.sleep(2)
    driver.save_screenshot("C:\\Users\\Surekha Gadhave\\PycharmProjects\\Demo123\\Screenshots\\"+filename+".png")

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


def test_progressbar():
    desired_cap = {
        "deviceName": "sdk_gphone64_x86_64",
        "platformName": "Android",
        "platformVersion": "13",
        "automationName": "UiAutomator2",
        "app": "C:\\Users\\Surekha Gadhave\\Downloads\\AndroidUI.apk"    #for this apk currently not able to click continue button.

    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    driver.implicitly_wait(5)
    obj=driver.find_element(By.ID,"")
    val1=driver.find_element(By.ID).text
    print(val1)
    action=TouchAction(driver)
    action.long_press(obj).move_to(obj,250,250).release().perform()
    val2 = driver.find_element(By.ID).text
    print(val2)


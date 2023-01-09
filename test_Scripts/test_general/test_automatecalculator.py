import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from POM.General import General


@allure.story("appium demo")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("automatecalculator")
def test_calculator():
    with allure.step("automate"):
        desired_cap = {
            "appium:deviceName": "Redmi Note 8",
            "platformName": "Android",
            "appium:platformVersion": "10",
            "appPackage": "com.google.android.calculator",
            "appActivity": "com.android.calculator2.Calculator"
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        driver.implicitly_wait(4)
        gs=General(driver)
        print("welcome to calculator")
        gs.click_seven()
        gs.click_add()
        gs.click_three()
        gs.click_equal()
        value=gs.get_finalresult()
        assert value == "10", "Calculator not working correctly"
        print("Calculator working perfectly")
        allure.attach(driver.get_screenshot_as_png(), name="Dialscreen", attachment_type=AttachmentType.PNG)

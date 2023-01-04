from appium import webdriver
from POM.General import General


def test_calculator():
    desired_cap = {
        "appium:deviceName": "sdk_gphone64_x86_64",
        "platformName": "Android",
        "appium:platformVersion": "13",
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
    driver.quit()
# test_calculator()
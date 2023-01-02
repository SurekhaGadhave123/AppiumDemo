import time
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from POM.meesho import Meesho


def test_scrollaction():
    desired_cap = {
        "appium:deviceName": "sdk_gphone64_x86_64",
        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:app": "C:\\Users\\Surekha Gadhave\\Downloads\\meesho-14-0.apk"}

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    driver.implicitly_wait(5)
    ms = Meesho(driver)
    # ms.click_continue()
    ms.click_close_window()
    ms.click_allow()
    print("welcome to Home page of meesho")
    ms.click_categories()
    time.sleep(3)
    print("welcome to categories page of meesho")

    for i in range(6):
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x=549, y=1701)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(x=549, y=567)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(3)
    print("Scrolling action performed successfully")
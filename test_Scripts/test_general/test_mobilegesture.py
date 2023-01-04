import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By

from POM.General import General


def test_mobilegesture():

        desired_cap = {
                "deviceName": "sdk_gphone64_x86_64",
                "platformName": "Android",
                "platformVersion": "13",
                "automationName": "UiAutomator2",
                "appPackage": "com.google.android.dialer",
                "appActivity": "com.google.android.dialer.extensions.GoogleDialtactsActivity",
                "newCommandTimeout":600
        }
        driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
        driver.implicitly_wait(30)
        gs = General(driver)
        gs.click_contacts()
        create=driver.find_element(By.ID,"com.google.android.dialer:id/empty_content_view_action")
        user_action=TouchAction(driver)
        user_action.tap(create).perform()
        gs.click_morefield()
        firstname = driver.find_element(By.XPATH, "//android.widget.EditText[@text='First name']")
        company=driver.find_element(By.XPATH,"//android.widget.EditText[@text='Company']")
        # scrolldown
        actions = ActionChains(driver)
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to(company)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to(firstname)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        time.sleep(3)
        firstname.send_keys("Appium Testing")
        time.sleep(2)
        user_action.long_press(firstname,duration=3000).perform()
        # hide keyboard
        driver.hide_keyboard()









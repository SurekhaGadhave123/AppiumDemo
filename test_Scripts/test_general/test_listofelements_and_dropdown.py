import time
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from selenium.webdriver.common.by import By
from POM.meesho import Meesho

@allure.story("appium demo")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("dropdown")
def test_dropdown():
    with allure.step("automate"):
        desired_cap = {
                "appium:deviceName": "Redmi Note 8",
                "platformName": "Android",
                "appium:platformVersion": "10",
                "appium:app": "C:\\Users\\Surekha Gadhave\\Downloads\\meesho-14-0.apk"}

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
        # driver.implicitly_wait(5)
        ms = Meesho(driver)
        # ms.click_continue()
        # time.sleep(3)
        # ms.click_close_window()
        driver.find_element(By.ID, "com.meesho.supply:id/close").click()
        # ms.click_allow()
        print("welcome to Home page of meesho")
        ms.click_account()
        ms.click_signup()
        useanothermobno=driver.find_element(By.ID,"com.truecaller:id/continueWithDifferentNumber")
        useanothermobno.click()
        driver.find_element(By.ID,"com.google.android.gms:id/cancel").click()
        ms.click_countrycode()
        # time.sleep(2)
        options=driver.find_elements(By.CLASS_NAME,"android.widget.TextView")
        print("elements:",len(options))
        # expected_list=['🇦🇫     Afghanistan (+93)', '🇦🇱     Albania (+355)', '🇩🇿     Algeria (+213)', '🇦🇸     American Samoa (+1)', '🇦🇩     Andorra (+376)', '🇦🇴     Angola (+244)', '🇦🇮     Anguilla (+1)', '🇦🇬     Antigua (+1)', '🇦🇷     Argentina (+54)', '🇦🇲     Armenia (+374)', '🇦🇼     Aruba (+297)', '🇦🇺     Australia (+61)']
        list=[]
        for option in options:
            list.append(option.get_attribute('text'))

        print(list)
        ms.click_country("🇦🇫     Afghanistan (+93)")
        print("Dropdown handled successfully")
        allure.attach(driver.get_screenshot_as_png(), name="screen", attachment_type=AttachmentType.PNG)
        driver.quit()
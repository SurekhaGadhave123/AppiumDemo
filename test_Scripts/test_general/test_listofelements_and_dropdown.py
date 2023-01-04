import time
from appium import webdriver
from selenium.webdriver.common.by import By
from POM.meesho import Meesho


def test_dropdown():
    desired_cap = {
        "appium:deviceName": "sdk_gphone64_x86_64",
        "platformName": "Android",
        "appium:platformVersion": "13",
        "appium:app": "C:\\Users\\Surekha Gadhave\\Downloads\\meesho-14-0.apk"}

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    driver.implicitly_wait(5)
    ms = Meesho(driver)
    # ms.click_continue()
    time.sleep(3)
    ms.click_close_window()
    ms.click_allow()
    print("welcome to Home page of meesho")
    ms.click_account()
    ms.click_signup()
    ms.click_countrycode()
    time.sleep(2)
    options=driver.find_elements(By.CLASS_NAME,"android.widget.TextView")
    print("elements:",len(options))
    expected_list=['🇦🇫     Afghanistan (+93)', '🇦🇱     Albania (+355)', '🇩🇿     Algeria (+213)', '🇦🇸     American Samoa (+1)', '🇦🇩     Andorra (+376)', '🇦🇴     Angola (+244)', '🇦🇮     Anguilla (+1)', '🇦🇬     Antigua (+1)', '🇦🇷     Argentina (+54)', '🇦🇲     Armenia (+374)', '🇦🇼     Aruba (+297)', '🇦🇺     Australia (+61)']
    list=[]
    for option in options:
        list.append(option.get_attribute('text'))

    print(list)
    assert expected_list==list,"list are not matching"
    # select country from dropdown
    ms.click_country("🇩🇿     Algeria (+213)")
    print("Dropdown handeled successfully")
    driver.quit()
import time
from appium import webdriver
from POM.General import General
from library.randomdata import gen_random_mobno


def test_send_msg():
    mobno=gen_random_mobno()
    desired_cap = {
        "deviceName": "sdk_gphone64_x86_64",
        "platformName": "Android",
        "platformVersion": "13",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    driver.implicitly_wait(5)
    gs=General(driver)
    gs.click_messegesicon()
    time.sleep(3)
    print("welcome to messaging app")
    gs.click_startchatbtn()
    gs.enter_phoneno(mobno)
    gs.click_creategroup()
    gs.click_next()
    msgtext="Hi how are u?"
    gs.enter_msg(msgtext)
    gs.click_sendbtn()
    time.sleep(3)
    sended_msg=gs.get_sended_msgtext()
    assert sended_msg==msgtext
    print("Sending messages working fine")
    driver.close()
test_send_msg()


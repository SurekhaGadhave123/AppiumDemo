from appium import webdriver

from POM.meesho import Meesho

desired_cap = {
  "appium:deviceName": "sdk_gphone64_x86_64",
  "platformName": "Android",
  "appium:platformVersion": "13",
  "appium:app": "C:\\Users\\Surekha Gadhave\\Downloads\\meesho-14-0.apk"
}
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)
driver.implicitly_wait(30)
ms = Meesho(driver)
# ms.click_continue()
ms.click_close_window()
ms.click_allow()
print("welcome to Home page of meesho")
driver.quit()
import time
from library.wrapper import Wrapper
from selenium.webdriver.common.by import By
class Meesho(Wrapper):
    def __init__(self, driver):
        super().__init__(driver)

    def click_close_window(self):
        close = (By.ID, "com.meesho.supply:id/close")
        self.click_element(close)
        time.sleep(2)

    def click_allow(self):
        allow = (By.ID, "com.android.permissioncontroller:id/permission_allow_button")
        self.click_element(allow)
        time.sleep(2)

    def click_women(self):
        women = (By.ID, "com.meesho.supply:id/item_widget_high_level")
        self.click_element(women)
        time.sleep(2)

    def click_kurties(self):
        kurties = (By.ID, "com.meesho.supply:id/title")
        self.click_element(kurties)
        time.sleep(2)

    def click_product(self):
        product = (By.ID, "com.meesho.supply:id/catalog_cover")
        self.click_element(product)
        time.sleep(2)

    def click_categories(self):
        categories = (By.ID, "com.meesho.supply:id/action_categories")
        self.click_element(categories)
        time.sleep(2)

    def click_continue(self):
        continue_btn =(By.ID, "com.meesho.supply:id/sign_up")
        self.click_element(continue_btn)
        time.sleep(2)


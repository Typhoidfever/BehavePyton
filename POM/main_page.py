from selenium.webdriver.common.by import By
from POM.login_page import Loginpage


class Mainpage:
    URL = "https://letcode.in"
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//a[text()='Log in']")
    LOCATOR_SIGN_OUT_BUTTON = (By.XPATH, "//a[text()='Sign out']")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)

    def click_sign_in(self):
        self.driver.find_element(*self.LOCATOR_LOGIN_BUTTON).click()
        self.driver.implicitly_wait(5)
        return Loginpage(self.driver)

    def sign_out_is_present(self):
        self.driver.find_element(*self.LOCATOR_SIGN_OUT_BUTTON).is_displayed()

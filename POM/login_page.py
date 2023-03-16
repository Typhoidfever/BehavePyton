from selenium.webdriver.common.by import By


class Loginpage:

    LOCATOR_LOGIN_FIELD = (By.CSS_SELECTOR, "[name=email]")
    LOCATOR_PASSWORD_FIELD = (By.CSS_SELECTOR, "[name=password]")
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//button[text()='LOGIN']")

    def __init__(self, driver):
        self.driver = driver

    def perform_authorization(self, login, password):

        self.driver.find_element(*self.LOCATOR_LOGIN_FIELD).send_keys(login)
        self.driver.find_element(*self.LOCATOR_PASSWORD_FIELD).send_keys(password)
        self.driver.implicitly_wait(5)

    def click_login(self):

        self.driver.find_element(*self.LOCATOR_LOGIN_BUTTON).click()
        self.driver.implicitly_wait(5)



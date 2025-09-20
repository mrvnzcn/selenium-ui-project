from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    PATH = "/login"
    USERNAME_INPUT = (By.ID,"username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def load(self):
        self.open(self.PATH)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_flash_message(self):
        return self.driver.find_element(*self.FLASH_MESSAGE).text

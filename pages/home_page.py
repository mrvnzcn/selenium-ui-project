from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    PATH = "/"
    ABTEST_LINK = (By.CSS_SELECTOR, "a[href='/abtest']")
    SUBTITLE = (By.TAG_NAME,"h2")
    TITLE = (By.CSS_SELECTOR,"h1.heading")

    def load(self):
        self.open(self.PATH)

    def get_header_text(self):
        return self.driver.find_element(*self.TITLE).text
    
    def get_subtitle_text(self):
        return self.driver.find_element(*self.SUBTITLE).text
    
    def click_ab_test(self):
        self.driver.find_element(*self.ABTEST_LINK).click()

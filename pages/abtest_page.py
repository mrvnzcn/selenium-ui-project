from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ABTestPage(BasePage):
    PATH = "/abtest"
    TITLE = (By.TAG_NAME,"h3")

    def load(self):
        self.open(self.PATH)
    
    def get_header_text(self):
        return self.driver.find_element(*self.TITLE).text
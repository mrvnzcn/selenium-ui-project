from pages.login_page import LoginPage
from faker import Faker


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("tomsmith", "SuperSecretPassword!")
    message = login_page.get_flash_message()
    assert "You logged into a secure area!" in message


fake = Faker()

def test_unsuccessful_login(driver):
    login_page = LoginPage(driver)
    login_page.load()

    # Rastgele kullanıcı adı ve şifre
    username = fake.user_name()
    password = fake.password()

    login_page.login(username, password)
    message = login_page.get_flash_message()

    assert "Your username is invalid!" in message

from pages.login_page import LoginPage
from testdata import credentials, messages, generators


def test_successful_login(driver, base_url):
    login_page = LoginPage(driver, base_url)
    login_page.load()
    login_page.login(credentials.VALID_USERNAME,credentials.VALID_PASSWORD)
    message = login_page.get_flash_message()
    assert messages.SUCCESS_LOGIN_MESSAGE in message

def test_unsuccessful_login(driver,base_url):
    login_page = LoginPage(driver,base_url)
    login_page.load()

    # Rastgele kullanıcı adı ve şifre
    username = generators.random_username()
    password = generators.random_username()

    login_page.login(username, password)
    message = login_page.get_flash_message()

    assert messages.INVALID_LOGIN_MESSAGE in message

from pages.home_page import HomePage

def test_home_page_headers(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.load()

    header_text = home_page.get_header_text()
    assert header_text == "Welcome to the-internet"

    subtitle_text = home_page.get_subtitle_text()
    assert subtitle_text == "Available Examples"

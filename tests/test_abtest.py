from pages.home_page import HomePage
from pages.abtest_page import ABTestPage


def test_abtest_navigation(driver, base_url):
    home_page = HomePage(driver, base_url)
    home_page.load()
    home_page.click_ab_test()

    ab_test_page  = ABTestPage(driver, base_url)

    assert driver.current_url == f"{base_url}/abtest"
    
    header = ab_test_page.get_header_text()
    valid_headers = ["A/B Test Variation 1", "A/B Test Control"]

    assert header in valid_headers

import pytest
from utils.browser_setup import get_driver
from pages.home_page import HomePage
from pages.result_page import ResultPage


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_longest_substring(driver):
    home = HomePage(driver)
    home.open()

    home.enter_input("abcabcbb")
    home.click_submit()

    result = ResultPage(driver)
    output = result.get_output()

    assert output == "3", f"Expected 3 but got {output}"

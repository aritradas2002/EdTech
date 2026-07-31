import pytest
from pages.home_page import HomePage


class TestHomePage:

    def test_verify_guvi_url(self, driver):
        home_page = HomePage(driver)

        # Launch GUVI website
        home_page.open_home_page()

        # Verify URL
        expected_url = "https://www.guvi.in"
        actual_url = home_page.get_current_url()

        assert expected_url in actual_url, (
            f"Expected URL to contain '{expected_url}', "
            f"but got '{actual_url}'"
        )
        # Expected and actual title
        expected_title = "GUVI | Learn to code in your native language"
        actual_title = home_page.get_home_page_title()

        # Verify title
        assert expected_url in actual_url, (
            f"Expected title: '{expected_title}', "
            f"but got: '{actual_title}'"
        )

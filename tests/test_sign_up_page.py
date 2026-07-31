import pytest
from pages.Sign_up_page import SignUpPage


class TestSignUpPage:

    def test_verify_sign_up_button(self, driver):
        sign_up_page = SignUpPage(driver)

        # Open GUVI Home Page
        sign_up_page.open_home_page()

        # Verify Sign-Up button is visible
        assert sign_up_page.is_sign_up_button_visible(), \
            "Sign-Up button is not visible."

        # Click Sign-Up button
        sign_up_page.click_sign_up_button()

        # Verify redirection
        expected_url = "https://www.guvi.in/register/"
        actual_url = driver.current_url

        assert expected_url in actual_url, (
            f"Expected URL: '{expected_url}', "
            f"but got: '{actual_url}'"
        )
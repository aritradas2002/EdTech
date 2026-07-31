from pages.login_page import LoginPage
from pages.home_page import HomePage


class TestLogout:

    def test_logout(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)

        login_page.open_home_page()
        login_page.click_login_button()
        login_page.login("aritradas546@gmail.com", "Aritra2002@")

        # Open profile menu
        home_page.click_profile_icon()

        # Logout
        home_page.click_logout()

        # Verify user is logged out
        assert home_page.is_login_button_visible()
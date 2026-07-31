from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


class TestHomePage:

    def test_verify_login_button(self, driver):

        login_page = LoginPage(driver)

        # Open GUVI homepage
        login_page.open_home_page()

        assert driver.find_element(
            By.XPATH,
            "//div[@class='⭐️f6lmuc-0 flex items-center gap-2 xl:gap-4']//button[@id='login-btn']"
        ).is_displayed()


        # Click Login button
        login_page.click_login_button()

        # Verify navigation to login page
        assert "sign-in" in login_page.get_current_url().lower(), \
            f"Expected login page, but current URL is: {login_page.get_current_url()}"

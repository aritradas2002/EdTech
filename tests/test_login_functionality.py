from selenium.webdriver.common.by import By

from pages.login_page import LoginPage


class TestLogin:

    def test_valid_login(self, driver):
        login_page = LoginPage(driver)

        login_page.open_home_page()
        login_page.click_login_button()
        login_page.login("aritradas546@gmail.com", "Aritra2002@")
        assert driver.find_element(By.XPATH,"//div[@class='⭐️f6lmuc-0 flex items-center gap-2 xl:gap-4']//div[@class='⭐️3hk5qd-0 btn bg-white shadow-none border-white hover:bg-white hover:border-white account p-0 w-max']//img[@alt='Profile']").is_displayed()




    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)

        login_page.open_home_page()
        login_page.click_login_button()
        login_page.login("invalid@gmail.com", "wrongpassword")

        assert login_page.get_error_message() in "Incorrect"
from pages.home_page import HomePage


class TestMenu:

    def test_verify_menu_items(self, driver):
        home_page = HomePage(driver)

        home_page.open_home_page()

        assert home_page.is_courses_visible()
        assert home_page.is_live_classes_visible()
        assert home_page.is_practice_visible()

    def test_verify_dobby_assistant(self, driver):
        home_page = HomePage(driver)

        home_page.open_home_page()


from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    URL = "https://www.guvi.in"
    COURSES = (By.XPATH, "//p[@class='⭐️f6lmuc-0 menu-hover text-sm font-medium text-nowrap leading-6'][normalize-space()='Courses']")
    LIVE_CLASSES = (By.XPATH, "//p[@class='⭐️f6lmuc-0 menu-hover text-sm font-medium text-nowrap leading-6'][normalize-space()='LIVE Classes']")
    PRACTICE = (By.XPATH, "//p[@class='⭐️f6lmuc-0 menu-hover text-sm font-medium text-nowrap leading-6'][normalize-space()='Practice']")
    PROFILE_ICON = (By.XPATH, "//div[@class='⭐️f6lmuc-0 flex items-center gap-2 xl:gap-4']//div[@class='⭐️3hk5qd-0 btn bg-white shadow-none border-white hover:bg-white hover:border-white account p-0 w-max']//img[@alt='Profile']")  # Replace with the correct locator
    LOGOUT_BUTTON = (By.XPATH, "//ul[@id='account-boxheader']//div[@id='signout']")
    LOGIN_BUTTON = (By.ID, "login-btn")

    # Replace the locator with the actual one after inspecting the page.

    def open_home_page(self):
        self.open_url(self.URL)

    def verify_home_page(self):
        return self.driver.current_url.startswith(self.URL)

    def get_home_page_title(self):
        return self.driver.title

    def is_courses_visible(self):
      return self.is_element_visible(self.COURSES)

    def is_live_classes_visible(self):
       return self.is_element_visible(self.LIVE_CLASSES)

    def is_practice_visible(self):
       return self.is_element_visible(self.PRACTICE)

    def click_profile_icon(self):
        self.click(self.PROFILE_ICON)

    def click_logout(self):
        self.click(self.LOGOUT_BUTTON)

    def is_login_button_visible(self):
        return self.is_element_visible(self.LOGIN_BUTTON)



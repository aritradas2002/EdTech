from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignUpPage(BasePage):

    URL = "https://www.guvi.in"

    SIGN_UP_BUTTON = (By.XPATH, "//div[@class='⭐️f6lmuc-0 flex items-center gap-2 xl:gap-4']//button[normalize-space()='Sign up']")

    def open_home_page(self):
        self.open_url(self.URL)

    def is_sign_up_button_visible(self):
        return self.is_element_visible(self.SIGN_UP_BUTTON)

    def click_sign_up_button(self):
        self.click(self.SIGN_UP_BUTTON)
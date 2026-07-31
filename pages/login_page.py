from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.guvi.in"

    # Home Page
    LOGIN_BUTTON = (By.XPATH, "//div[@class='⭐️f6lmuc-0 flex items-center gap-2 xl:gap-4']//button[@id='login-btn']")

    # Login Page
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "login-btn")
    profile_icon = (By.XPATH, "//div[@class='⭐️f6lmuc-0 flex items-center gap-2 xl:gap-4']//div[@class='⭐️3hk5qd-0 btn bg-white shadow-none border-white hover:bg-white hover:border-white account p-0 w-max']//img[@alt='Profile']")

    ERROR_MESSAGE = (
        By.XPATH,
        "//div[contains(@class,'invalid-feedback') or contains(text(),'Incorrect')]"
    )

    PROFILE_ICON = (
        By.XPATH,
        "//div[@class='⭐️f6lmuc-0 flex items-center gap-2 xl:gap-4']//div[@class='⭐️3hk5qd-0 btn bg-white shadow-none border-white hover:bg-white hover:border-white account p-0 w-max']//img[@alt='Profile']"
    )

    def open_home_page(self):
        self.open_url(self.URL)

    def is_login_button_visible(self):
        self.is_element_visible(self.LOGIN_BUTTON)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def enter_email(self, email):
        self.enter_text(self.EMAIL, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD, password)

    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit()


    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)






from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url



    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)


    def get_text(self, locator):
      return self.driver.find_element(*locator).text

    def is_element_visible(self, locator):
        try:
            print(f"Searching for: {locator}")

            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            print("Element found.")
            return element.is_displayed()

        except Exception as e:
            print(e)
            return False
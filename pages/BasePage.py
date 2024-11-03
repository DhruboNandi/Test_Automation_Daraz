from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        # Add a wait here to ensure element is present
        wait = WebDriverWait(self.driver, 15)

        if "_id:" in locator:
            return wait.until(EC.presence_of_element_located((By.ID, locator.split(":")[1])))
        elif "_name:" in locator:
            return wait.until(EC.presence_of_element_located((By.NAME, locator.split(":")[1])))
        elif "_class_name:" in locator:
            return wait.until(EC.presence_of_element_located((By.CLASS_NAME, locator.split(":")[1])))
        elif "_css_selector:" in locator:
            return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator.split(":")[1])))
        elif "_xpath:" in locator:
            return wait.until(EC.presence_of_element_located((By.XPATH, locator.split(":")[1])))
        elif "_link_text:" in locator:
            return wait.until(EC.presence_of_element_located((By.LINK_TEXT, locator.split(":")[1])))
        elif "_partial_link_text:" in locator:
            return wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, locator.split(":")[1])))
        elif "_tag_name:" in locator:
            return wait.until(EC.presence_of_element_located((By.TAG_NAME, locator.split(":")[1])))

        raise ValueError(f"Unsupported locator type: {locator}")

    def is_element_present(self, locator):
        try:
            self.get_element(locator)
            return True
        except NoSuchElementException:
            return False

    def click_on_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def type(self, text, locator):
        element = self.get_element(locator)
        element.clear()
        element.click()
        element.send_keys(text)

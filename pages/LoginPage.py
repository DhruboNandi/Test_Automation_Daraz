from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    phone_number_id = "_id:phone"

    def enter_phone_number(self, phone_number):
        self.driver.find_element(By.ID, self.phone_number_id).click()
        self.driver.find_element(By.ID, self.phone_number_id).clear()
        self.driver.find_element(By.ID, self.phone_number_id).send_keys(phone_number)

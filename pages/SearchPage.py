import self

from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #XPath for search
    valid_Honestime_Presents_Tenda = "Honestime Presents "
    #no_search_result = self.driver.find_element(By.CLASS_NAME, "jG0xV")
    no_search_result = "jG0xV"
    #no_search_result = //*[contains(@class, 'jG0xV')]
    #no_search_result = self.driver.find_element(By.XPATH, "//*[contains(@class, 'jG0xV')]")

    search_for_no_product = "p-mod-card-content"

    def display_status_of_product(self):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, self.valid_Honestime_Presents_Tenda).is_displayed()

    def no_search_result_text(self):
        return self.driver.find_element(By.CLASS_NAME, self.no_search_result).text

    def search_for_no_product(self):
        return self.driver.find_element(By.CLASS_NAME, self.search_for_no_product)

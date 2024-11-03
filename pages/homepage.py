import self
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver

from pages.BasePage import BasePage
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    driver: webdriver

    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_id = "_id:q"
    #search_box_field_id = "_id:q"
    search_button_click = "search-box__button--1oH7"
    #search_button_click_class_name = "_class_name:search-box__button--1oH7"
    # XPath for become_a_seller
    become_a_seller = "_id:topActionSell"
    create_a_new_acc = "_link_text:Create a new account"
    enter_phone_number_box = "phone"


    def enter_product_into_search_box_filed(self, product_name):
        self.type(product_name, self.search_box_field_id)
        # self.driver.find_element(By.ID, self.search_box_field_id).click()
        # self.driver.find_element(By.ID, self.search_box_field_id).clear()
        # self.driver.find_element(By.ID, self.search_box_field_id).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.CLASS_NAME, self.search_button_click).click()

    # def click_on_search_button(self):
    #     self.click_on_element(self.search_button_click)
    #     return SearchPage(self.driver)

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_filed(product_name)
        self.click_on_search_button()
        return SearchPage(self.driver)

    def enter_phn_number(self):
        self.driver.find_element(By.ID, self.enter_phone_number_box).send_keys("0187124178")

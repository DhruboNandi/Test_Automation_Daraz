import time
from telnetlib import EC

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.LoginPage import LoginPage
from pages.homepage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSeller:
    driver: WebDriver

    def test_valid_signup(self):
        home_page= HomePage(self.driver)
        home_page.click_on_element(home_page.become_a_seller)
        home_page.click_on_element(home_page.create_a_new_acc)
        login_page = LoginPage(self.driver)
        time.sleep(5)
        login_page.enter_phone_number("0199991291")
        time.sleep(5)

    def test_invalid_signup(self):
        home_page = HomePage(self.driver)
        home_page.click_on_element(home_page.become_a_seller)
        home_page.click_on_element(home_page.create_a_new_acc)
        login_page = LoginPage(self.driver)
        time.sleep(5)
        login_page.enter_phone_number("019")
        expected_text = "Invalid account or password."
        assert self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]").text.__eq__(expected_text)
        time.sleep(5)


import time

import pytest
import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.SearchPage import SearchPage
from pages.homepage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    driver: WebDriver

    def test_search_for_valid_product(self):
        home_page = HomePage(self.driver)
        search_product = home_page.search_for_a_product("Honestime Presents Tenda F3 300mbps 3 Antennas Router")
        time.sleep(5)
        assert search_product.display_status_of_product()

    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        search_product= home_page.search_for_a_product("a")
        time.sleep(5)
        expected_text = "Search No Result"
        actual_text = search_product.no_search_result_text()
        assert actual_text == expected_text

    def test_search_for_without_entering_product(self):
        home_page = HomePage(self.driver)
        home_page.click_on_search_button()
        assert self.driver.find_element(By.ID, home_page.search_box_field_id)
        time.sleep(5)

import time

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from pages.CartPage import CartPage
from pages.homepage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestAddCart:
    driver: WebDriver

    def test_add_to_cart(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("hp")
        add_cart = CartPage(self.driver)
        click_product = home_page.click_on_element(add_cart.click_selected_product)
        home_page.click_on_element(add_cart.add_to_cart_button)
        assert home_page.is_element_present(add_cart.enter_phonenum_or_email)


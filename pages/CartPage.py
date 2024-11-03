from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    click_selected_product = "_xpath://div[@data-qa-locator='product-item'][2]"
    add_to_cart_button = "_css_selector:button.add-to-cart-buy-now-btn.pdp-button_theme_orange"
    enter_phonenum_or_email ="_xpath://input[@class='iweb-input' and @placeholder='Please enter your Phone Number or Email']"

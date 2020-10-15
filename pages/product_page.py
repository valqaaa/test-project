from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    go_to_product_page_locator =  "li:nth-child(1) > article > h3 > a"
    add_book_submit_locator = "btn-add-to-basket"
    message_locator = "alertinner"
    message1 = "has been added to your basket"
    message2 = "please sign in"

    def go_to_product_page(self):
        open_product_page = self.browser.find_element(By.CSS_SELECTOR, ProductPage.go_to_product_page_locator)
        open_product_page.click()

    def add_product_from_product_page(self):
        add_book = self.browser.find_element(By.CLASS_NAME, ProductPage.add_book_submit_locator)
        add_book.click()

    def check_success_message_of_added_product(self):
        success_message = self.browser.find_element(By.CLASS_NAME, ProductPage.message_locator)
        assert ProductPage.message1 in success_message.text, \
            f"Success message doesn't correct"

    def check_message_for_unauthorized_user(self):
        unauthorized_message = self.browser.find_element(By.CLASS_NAME, ProductPage.message_locator)
        assert ProductPage.message2 in unauthorized_message.text, \
            f"Product's name doesn't match"

from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    main_page_link = "http://selenium1py.pythonanywhere.com/"
    login_link = "#login_link"
    product_page_link = "#browse > li > ul > li:nth-child(1) > a"
    basket_page_link = "span > a"

    def __init__(self, browser):
        BasePage.__init__(self, browser, MainPage.main_page_link)

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, MainPage.login_link)
        login_link.click()

    def go_to_products_catalog_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, MainPage.product_page_link)
        login_link.click()

    def go_to_basket_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, MainPage.basket_page_link)
        login_link.click()

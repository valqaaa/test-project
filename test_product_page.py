import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


# 1. User can add product to basket

def test_user_can_add_product_to_basket(browser):
    # Arrange
    main_page = MainPage(browser)
    main_page.open()

    # Act
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.sign_in()
    main_page.go_to_products_catalog_page()
    product_page = ProductPage(browser, browser.current_url)
    product_page.go_to_product_page()
    product_page.add_product_from_product_page()

    # Assert
    product_page.check_success_message_of_added_product()


# 2. Guest can add product to basket

def test_guest_can_add_product_to_basket(browser):
    # Arrange
    main_page = MainPage(browser)
    main_page.open()

    # Act
    main_page.go_to_products_catalog_page()
    product_page = ProductPage(browser, browser.current_url)
    product_page.go_to_product_page()
    product_page.add_product_from_product_page()

    # Assert
    product_page.check_success_message_of_added_product()


# 3. Guest can't see product in basket opened from product page

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # Arrange
    main_page = MainPage(browser)
    main_page.open()

    # Act
    main_page.go_to_products_catalog_page()
    product_page = ProductPage(browser, browser.current_url)
    product_page.go_to_product_page()
    product_page.add_product_from_product_page()
    main_page.go_to_basket_page()

    # Assert
    #product_page.check_message_for_unauthorized_user()


# 4. Guest can go to login page from product_page

def test_guest_can_go_to_login_page_from_product_page(browser):
    # Arrange
    main_page = MainPage(browser)
    main_page.open()

    # Act
    main_page.go_to_products_catalog_page()
    main_page.go_to_login_page()

    # Assert
    #product_page.check_success_message_of_added_product()

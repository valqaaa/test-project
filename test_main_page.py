import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage


# 1. Registration
@pytest.mark.need_review_custom_scenarios
def test_sign_up(browser):
    # Arrange
    main_page = MainPage(browser)
    main_page.open()

    # Act
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.create_new_user()

    # Assert
    login_page.check_success_sign_up_message()

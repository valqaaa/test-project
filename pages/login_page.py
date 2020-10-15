from .base_page import BasePage
import random
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    sign_up_email_input_locator = "id_registration-email"
    sign_up_password_input_locator = "id_registration-password1"
    confirm_sign_up_password_input_locator = "id_registration-password2"
    password_1 = "karandash123"
    sign_up_submit_locator = "registration_submit"
    success_sigh_up_message = "Спасибо за егистрацию!"
    success_message_locator = "alertinner"

    sign_in_locator = "login_link"
    login = "pojim23044@inxto.ru"
    password_2 = "karandash1234"
    sign_in_login_input_locator = "id_login-username"
    sign_in_password_input_locator = "id_login-password"
    sign_in_submit_locator = "login_submit"
    success_sign_in_message = "Welcome back"

    def create_new_user(self):
        domen = ""
        email = ""
        for x in range(12):
            domen = domen + random.choice(list("1234567890qwertyuiopasdfghjklzxcvbnm"))
            email = domen + "@" + "mail.ru"
        print(email)

        email_input = self.browser.find_element(By.ID, LoginPage.sign_up_email_input_locator)
        email_input.send_keys(email)
        password_input = self.browser.find_element(By.ID, LoginPage.sign_up_password_input_locator)
        password_input.send_keys(LoginPage.password_1)
        confirm_password_input = self.browser.find_element(By.ID, LoginPage.confirm_sign_up_password_input_locator)
        confirm_password_input.send_keys(LoginPage.password_1)
        confirm_registration_button = self.browser.find_element(By.NAME, LoginPage.sign_up_submit_locator)
        confirm_registration_button.click()

    def check_success_sign_up_message(self):
        success_message = self.browser.find_element_by_class_name(LoginPage.success_message_locator)
        assert LoginPage.success_sigh_up_message in success_message.text, \
            f"Sign up page should contain valid success message"

    def sign_in(self):
        sigh_in_button = self.browser.find_element(By.ID, LoginPage.sign_in_locator)
        sigh_in_button.click()
        login_input = self.browser.find_element(By.ID, LoginPage.sign_in_login_input_locator)
        login_input.send_keys(LoginPage.login)
        password_input = self.browser.find_element(By.ID, LoginPage.sign_in_password_input_locator)
        password_input.send_keys(LoginPage.password_1)
        confirm_sugn_button = self.browser.find_element_by_name(LoginPage.sign_in_submit_locator)
        confirm_sugn_button.click()

    def check_success_sign_in_message(self):
        success_message = self.browser.find_element_by_class_name(LoginPage.success_message_locator)
        assert LoginPage.success_sign_in_message in success_message.text, \
            f"Sign in page should contain valid success message"

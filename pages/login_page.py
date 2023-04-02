from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Реализуйте проверку на корректный url адрес."""
        assert 'login' in self.browser.current_url, "The current url is missing 'login'"

    def should_be_login_form(self):
        """Реализуйте проверку, что есть форма логина."""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FROM), "Login form is missing"

    def should_be_register_form(self):
        """Реализуйте проверку, что есть форма регистрации на странице."""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FROM), "Registration form is missing"

    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*LoginPageLocators.EMAIL_FORM)
        email_form.send_keys(email)
        passwd_1 = self.browser.find_element(*LoginPageLocators.PASSWD_FORM_1)
        passwd_1.send_keys(password)
        passwd_2 = self.browser.find_element(*LoginPageLocators.PASSWD_FORM_2)
        passwd_2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

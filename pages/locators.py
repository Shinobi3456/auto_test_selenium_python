from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket-mini')]/span/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket-mini')]/span/a")


class LoginPageLocators:
    LOGIN_FROM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FORM = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWD_FORM_1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    PASSWD_FORM_2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main>p.price_color")
    NAME_PRODUCT = (By.TAG_NAME, "h1")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success strong")
    ALERT_BASKET = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) > .alertinner")


class BasketPageLocators:
    FORM_WITH_PRODUCTS = (By.CSS_SELECTOR, "div#content_inner > form.basket_summary")
    CONTAINER_BASKET = (By.CSS_SELECTOR, "div#content_inner")

    


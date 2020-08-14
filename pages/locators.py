from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators:
    LOGIN_FROM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main>p.price_color")
    NAME_PRODUCT = (By.TAG_NAME, "h1")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success strong")
    ALERT_BASKET = (By.CSS_SELECTOR, ".alert-info strong")
    


from .base_page import BasePage
from .locators import ProductPageLocators, MainPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        bnt_add_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        bnt_add_basket.click()
    
    def should_be_success_message(self):
        alerts = self.browser.find_elements(*ProductPageLocators.ALERT_SUCCESS)
        name_product_tag = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name = name_product_tag.text
        
        result = False
        for alert in alerts:
            if name == alert.text:
                result = True
                break
        
        assert result is True, 'The name of the product added to the cart does not match the name on the product card'
    
    def should_be_basket_price(self):
        alert = self.browser.find_element(*ProductPageLocators.ALERT_BASKET)
        product_price_teg = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        
        product_price = product_price_teg.text
        basket_price = alert.text
        
        assert product_price == basket_price, f'Price product {product_price} != Basket price {basket_price}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

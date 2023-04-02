from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        """Проверяем что мы на странице корзины"""
        self.should_be_basket_url()

    def should_be_basket_url(self):
        """Реализуйте проверку на корректный url адрес."""
        assert 'basket' in self.browser.current_url, "The current url is missing 'basket'"

    def should_be_not_product(self):
        """Ожидаем, что в корзине нет товаров."""
        assert not self.is_element_present(*BasketPageLocators.FORM_WITH_PRODUCTS), "Cart expected to be empty"

    def should_be_text_label_empty_basket(self):
        """Ожидаем, что есть текст о том что корзина пуста."""
        element = self.browser.find_element(*BasketPageLocators.CONTAINER_BASKET)
        result = 'Your basket is empty' in element.text or 'Ваша корзина пуста' in element.text
        assert result, "Text not found that cart is empty"



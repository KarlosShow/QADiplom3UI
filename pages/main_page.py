from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    def open_main_page(self, url):
        self.open(url)
    def open_feed_section(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_url_contains('/feed')
    def open_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)
    def open_ingredient_modal(self):
        self.click(MainPageLocators.FIRST_INGREDIENT)
    def close_ingredient_modal(self):
        self.click(MainPageLocators.CLOSE_MODAL_BUTTON)
    def add_ingredient_to_order(self):
        self.drag_element(
            MainPageLocators.FIRST_FILLING,
            MainPageLocators.BURGER_CONSTRUCTOR_AREA
        )
    def ingredient_modal_visible(self):
        return self.element_is_displayed(
            MainPageLocators.INGREDIENT_MODAL
        )
    def constructor_area_has_item(self):
        return self.element_is_displayed(
            MainPageLocators.CONSTRUCTOR_ITEM
        )

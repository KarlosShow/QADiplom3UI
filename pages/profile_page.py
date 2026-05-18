from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators

class ProfilePage(BasePage):
    def open_profile(self):
        self.click(ProfilePageLocators.PROFILE_BUTTON)
    def logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)
    def wait_profile_page(self):
        return self.element_is_displayed(
            ProfilePageLocators.PROFILE_HEADER
        )

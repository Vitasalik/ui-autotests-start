from playwright.sync_api import Page, expect

from components.authentification.registration_form_component import RegistrationFormComponent
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.registration_button = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')

    def open_page(self) -> None:
        super().visible(self.URL)

    def click_registration_button(self) -> None:
        expect(self.registration_button).to_be_visible()
        self.registration_button.click()

    def click_login_link(self) -> None:
        self.login_link.click()


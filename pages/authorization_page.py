from playwright.sync_api import Page, expect, Response
from pages.base_page import BasePage


class AuthorizationPage(BasePage):
    URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login"

    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id("login-form-email-input").locator("input")
        self.password_input = page.get_by_test_id("login-form-password-input").locator("input")
        self.login_button = page.get_by_test_id("login-page-login-button")
        self.wrong_email_or_password_alert = page.get_by_test_id("login-page-wrong-email-or-password-alert")

    def open_page(self) -> None:
        super().open(self.URL)

    def check_visible_authorization_form(self) -> None:
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.login_button).to_be_visible()

    def fill_authorization_form(self, email: str, password: str) -> None:
        self.email_input.fill(email)
        self.password_input.fill(password)

    def click_login_button(self) -> None:
        self.login_button.click()

    def check_wrong_alert(self) -> None:
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")

# def log_response(response: Response) -> None:
#    print(f"Response: {response.url}, {response.status}")

# def print_log_response(self) -> None:
#   self.page.on("response", log_response)

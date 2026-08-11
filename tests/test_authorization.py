from pages.login_page import LoginPage
import pytest


@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize("email,password",
                         [
                             ("user.name@gmail.com", "password"),
                             ("  ", "password"),
                             ("user.name@gmail.com", "  ")
                         ]
)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visible("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    login_page.login_form.fill_login_form(email, password)
    login_page.login_form.check_visible(email, password)
    login_page.click_login_button()
    login_page.check_visible_wrong_email_or_password_alert()

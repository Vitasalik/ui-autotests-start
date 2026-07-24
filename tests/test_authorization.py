import pytest

from pages.dashboard_page import DashboardPage
from pages.authorization_page import AuthorizationPage


@pytest.mark.ui
def test_authorization_wrong(user_data_wrong,
                             authorization_page: AuthorizationPage,
                             dashboard_page: DashboardPage) -> None:

    authorization_page.open_page()
    #authorization_page.print_log_response()
    authorization_page.check_visible_authorization_form()
    authorization_page.fill_authorization_form(email=user_data_wrong['email'],
                                               password=user_data_wrong['password'])
    authorization_page.click_login_button()
    



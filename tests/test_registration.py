import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage

@pytest.mark.ui
def test_successful_registration(user_data,
                                 registration_page: RegistrationPage,
                                 dashboard_page: DashboardPage):
        registration_page.open_page()
        registration_page.check_visible_registration_form()
        registration_page.fill_registration_page(email=user_data["email"],
                                                 username=user_data["username"],
                                                 password=user_data["password"])
        registration_page.click_registration_button()

        dashboard_page.check_opened()
        dashboard_page.check_visible_toolbar_title()

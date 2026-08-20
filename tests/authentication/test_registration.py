import pytest
import allure
from allure_commons.types import Severity

from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStory
from tools.allure.features import AllureFeature


@pytest.mark.registration
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, user_data,
                                     registration_page: RegistrationPage,
                                     dashboard_page: DashboardPage):
            registration_page.open_page()
            registration_page.registration_form.fill_registration_form(
                email=user_data["email"],
                username=user_data["username"],
                password=user_data["password"])
            registration_page.click_registration_button()

            dashboard_page.check_opened()
            dashboard_page.dashboard_toolbar.check_visible()

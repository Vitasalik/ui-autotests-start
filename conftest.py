import pytest
from playwright.sync_api import Page

from pages.authorization_page import AuthorizationPage
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage

@pytest.fixture
def user_data() -> dict[str, str]:
    return {
        "email": "user@example.com",
        "username": "testuser",
        "password": "password123"
    }
@pytest.fixture
def user_data_wrong() -> dict[str, str]:
    return {
        "email": "user.name@gmail.com",
        "password": "password"
    }

@pytest.fixture
def registration_page(page: Page) -> RegistrationPage:
    return RegistrationPage(page)

@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)

@pytest.fixture
def authorization_page(page: Page) -> AuthorizationPage:
    return AuthorizationPage(page)
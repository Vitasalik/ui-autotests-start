import pytest

pytest_plugins = (
    "fixtures.browsers",
    "fixtures.allure",
    "fixtures.pages",
)

@pytest.fixture
def user_data() -> dict[str, str]:
    return {
        "email": "user@example.com",
        "username": "testUser",
        "password": "password123"
    }
@pytest.fixture
def user_data_wrong() -> dict[str, str]:
    return {
        "email": "user.name@gmail.com",
        "password": "password"
    }

